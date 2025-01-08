from datetime import datetime, timedelta

from django.test import TestCase, Client
from django.urls import reverse

from django.db import models

from appointment.models import Eye, ResultOfService, Appointment, Schedule
from appointment.templatetags.appointment_tags import add_media
from config.settings import DEFAULT_BEGIN_TIME, DEFAULT_END_TIME
from optics.models import Service
from users.models import User


class AppointmentAppTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.eye = Eye.objects.create(sph=2.0)
        cls.result_of_service = ResultOfService.objects.create(recommendations='Result for test')
        cls.appointment = Appointment.objects.create(day="2025-01-05", time="10:00")
        cls.medic = User.objects.create(username="testmedic", password="testpass", is_medic=True)
        cls.service = Service.objects.create(name='Service for test', price=1.11)
        cls.service.medic.add(cls.medic)
        cls.schedule = Schedule.objects.create(day="2025-01-05", medic=cls.medic)

        cls.client = Client()
        cls.user = User.objects.create_user(username="testuser", password="testpass")

    def test_eye_model(self):
        eye=Eye.objects.get(id=self.eye.pk)

        field_label = Eye._meta.get_field('sph').verbose_name
        self.assertEqual(field_label,'SPH')
        field_label = Eye._meta.get_field('cyl').verbose_name
        self.assertEqual(field_label,'CYL')
        field_label = Eye._meta.get_field('ax').verbose_name
        self.assertEqual(field_label,'AX')
        field_label = Eye._meta.get_field('pr').verbose_name
        self.assertEqual(field_label,'Pr')
        field_label = Eye._meta.get_field('bas').verbose_name
        self.assertEqual(field_label,'BAS')
        field_label = Eye._meta.get_field('dp').verbose_name
        self.assertEqual(field_label,'DP')
        field_label = Eye._meta.get_field('add').verbose_name
        self.assertEqual(field_label,'ADD')

        for field in Eye._meta.get_fields():
            if type(field) == models.DecimalField:
                max_digits = field.max_digits
                self.assertEqual(max_digits,5)
                decimal_places = field.decimal_places
                self.assertEqual(decimal_places,2)

        expected_object_name = 'sph %s ..' % (eye.sph)
        self.assertEqual(expected_object_name,str(eye))

    def test_result_model(self):
        eye=ResultOfService.objects.get(id=self.eye.pk)

        field_label = ResultOfService._meta.get_field('od').verbose_name
        self.assertEqual(field_label,'OD')
        field_label = ResultOfService._meta.get_field('os').verbose_name
        self.assertEqual(field_label,'OS')
        field_label = ResultOfService._meta.get_field('recommendations').verbose_name
        self.assertEqual(field_label,'Рекомендации')
        field_label = ResultOfService._meta.get_field('comment').verbose_name
        self.assertEqual(field_label,'Комментарий')
        field_label = ResultOfService._meta.get_field('created_at').verbose_name
        self.assertEqual(field_label,'Создан')
        field_label = ResultOfService._meta.get_field('update_at').verbose_name
        self.assertEqual(field_label,'Изменен')

        expected_object_name = 'OD: %s, OS: %s' % (str(eye.od), str(eye.os))
        self.assertEqual(expected_object_name,str(eye))


    def test_appointment_model(self):
        appointment=Appointment.objects.get(id=self.appointment.pk)

        field_label = Appointment._meta.get_field('day').verbose_name
        self.assertEqual(field_label,'День')
        field_label = Appointment._meta.get_field('time').verbose_name
        self.assertEqual(field_label,'Время')
        field_label = Appointment._meta.get_field('comment').verbose_name
        self.assertEqual(field_label,'Комментарий')
        field_label = Appointment._meta.get_field('owner').verbose_name
        self.assertEqual(field_label,'Владелец')
        field_label = Appointment._meta.get_field('service').verbose_name
        self.assertEqual(field_label,'Услуга')
        field_label = Appointment._meta.get_field('medic').verbose_name
        self.assertEqual(field_label,'Медик')
        field_label = Appointment._meta.get_field('result').verbose_name
        self.assertEqual(field_label,'Результат')

        max_length = Appointment._meta.get_field('comment').max_length
        self.assertEqual(max_length, 100)

        expected_object_name = '%s %s (%s)' % (appointment.owner, appointment.service, appointment.day)
        self.assertEqual(expected_object_name,str(appointment))


    def test_schedule_model(self):
        schedule=Schedule.objects.get(id=self.schedule.pk)

        field_label = Schedule._meta.get_field('day').verbose_name
        self.assertEqual(field_label,'День')
        field_label = Schedule._meta.get_field('begin_time').verbose_name
        self.assertEqual(field_label,'Начало приема')
        field_label = Schedule._meta.get_field('end_time').verbose_name
        self.assertEqual(field_label,'Конец приема')
        field_label = Schedule._meta.get_field('is_working_day').verbose_name
        self.assertEqual(field_label,'Рабочий день')
        field_label = Schedule._meta.get_field('medic').verbose_name
        self.assertEqual(field_label,'Медик')

        self.assertEqual(schedule.begin_time, datetime.strptime(DEFAULT_BEGIN_TIME, '%H:%M').time())
        self.assertEqual(schedule.end_time, datetime.strptime(DEFAULT_END_TIME, '%H:%M').time())

        expected_object_name = '%s %s %s %s' % (schedule.medic, schedule.day, schedule.begin_time, schedule.end_time)
        self.assertEqual(expected_object_name,str(schedule))

    def test_day_of_week(self):
        schedule = Schedule.objects.get(id=self.schedule.pk)
        weekdays = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс']
        for i in range(7):
            schedule.day += timedelta(days=1)
            schedule.save()
            self.assertEqual(schedule.day_of_week, weekdays[i])


    def test_login_required_redirect(self):
        for i in range(1,5):
            response = self.client.get(reverse(f'appointment:step-{str(i)}'))
            self.assertEqual(response.status_code, 302)
            self.assertRedirects(response, f'/login/?next=/appointment/step-{str(i)}/')

    def test_views_steps(self):
        self.client.login(username='testuser', password='testpass')
        for i in range(1,3):
            url = reverse(f'appointment:step-{str(i)}')
            if i<=2:
                new_url = url + f'?service_pk={self.service.pk}&medic_pk={self.medic.pk}'
                response = self.client.get(new_url)
            else:
                response = self.client.post(url)
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, f'appointment/step_{str(i)}.html')


    def test_views_service_list_view(self):
        self.client.login(username='testuser', password='testpass')
        url = reverse('appointment:appointment-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'appointment/appointment-list.html')

    def test_views_appointment_detail(self):
        url = reverse('appointment:appointment-detail', args=[self.appointment.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'appointment/appointment-detail.html')

    def test_blog_tags(self):
        self.assertEqual(add_media(None), "#")
        self.assertEqual(add_media("test.img"), "/media/test.img")


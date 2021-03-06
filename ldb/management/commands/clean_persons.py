from __future__ import unicode_literals

from sys import stderr

from django.core.exceptions import ValidationError
from django.core.management import BaseCommand

from ldb.models import Alumnus, Member, Person, Student

BASE_URL = "https://dienst2.ch.tudelft.nl/ldb/people/"


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            "--no-persons",
            action="store_false",
            dest="clean-persons",
            default=True,
            help="Do not run full_clean for persons",
        )
        parser.add_argument(
            "--no-members",
            action="store_false",
            dest="clean-members",
            default=True,
            help="Do not run full_clean for members",
        )
        parser.add_argument(
            "--no-students",
            action="store_false",
            dest="clean-students",
            default=True,
            help="Do not run full_clean for students",
        )
        parser.add_argument(
            "--no-alumni",
            action="store_false",
            dest="clean-alumni",
            default=True,
            help="Do not run full_clean for alumni",
        )
        parser.add_argument(
            "--save",
            action="store_true",
            dest="save",
            default=False,
            help="Perform save on models",
        )

    def handle(self, *args, **options):
        persons = Person.objects.all().order_by("id")
        for person in persons:
            if options["clean-persons"]:
                try:
                    person.full_clean()
                    if options["save"]:
                        person.save()
                except ValidationError as e:
                    stderr.write(
                        f"Validation error in Person {BASE_URL}{person.id}/ - {e}\n"
                    )

            if options["clean-members"]:
                try:
                    person.member.full_clean()
                    if options["save"]:
                        person.member.save()
                except Member.DoesNotExist:
                    pass
                except ValidationError as e:
                    stderr.write(
                        f"Validation error in Member {BASE_URL}{person.id}/ - {e}\n"
                    )

            if options["clean-students"]:
                try:
                    person.student.full_clean()
                    if options["save"]:
                        person.student.save()
                except Student.DoesNotExist:
                    pass
                except ValidationError as e:
                    stderr.write(
                        f"Validation error in Student {BASE_URL}{person.id}/ - {e}\n"
                    )

            if options["clean-alumni"]:
                try:
                    person.alumnus.full_clean()
                    if options["save"]:
                        person.alumnus.save()
                except Alumnus.DoesNotExist:
                    pass
                except ValidationError as e:
                    stderr.write(
                        f"Validation error in Alumnus {BASE_URL}{person.id}/ - {e}\n"
                    )

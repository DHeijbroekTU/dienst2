# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-27 20:51
from __future__ import unicode_literals

import dienst2.extras
from django.db import migrations, models
import django.db.models.deletion
import ldb.country_field


class Migration(migrations.Migration):

    replaces = [('ldb', '0001_initial'), ('ldb', '0002_nulls'), ('ldb', '0003_uniqueness'), ('ldb', '0004_auto_20150611_1109'), ('ldb', '0005_index_upper'), ('ldb', '0006_gratuated_to_enrolled'), ('ldb', '0007_person_membership_status'), ('ldb', '0008_person_mail_educational'), ('ldb', '0009_organization_blank_name_prefix'), ('ldb', '0010_auto_20160612_2323'), ('ldb', '0011_auto_20160914_1529'), ('ldb', '0012_auto_20170106_1510')]

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Committee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('description', models.TextField(blank=True, verbose_name='description')),
            ],
            options={
                'verbose_name': 'committee',
                'verbose_name_plural': 'committees',
            },
        ),
        migrations.CreateModel(
            name='CommitteeMembership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('board', models.IntegerField(verbose_name='board')),
                ('position', models.CharField(blank=True, max_length=50, verbose_name='position')),
                ('ras_months', models.IntegerField(blank=True, null=True, verbose_name='RAS months')),
                ('committee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ldb.Committee')),
            ],
            options={
                'verbose_name': 'committee membership',
                'verbose_name_plural': 'committee memberships',
            },
        ),
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street_name', models.CharField(blank=True, max_length=75, verbose_name='street name')),
                ('house_number', models.CharField(blank=True, max_length=7, verbose_name='house number')),
                ('address_2', models.CharField(blank=True, max_length=75, verbose_name='address row 2')),
                ('address_3', models.CharField(blank=True, max_length=75, verbose_name='address row 3')),
                ('postcode', models.CharField(blank=True, max_length=10, verbose_name='postcode')),
                ('city', models.CharField(blank=True, max_length=50, verbose_name='city')),
                ('country', ldb.country_field.CountryField(blank=True, choices=[('AF', 'Afghanistan'), ('AX', 'Ålandseilanden'), ('AL', 'Albanië'), ('DZ', 'Algerije'), ('AS', 'Amerikaans-Samoa'), ('AD', 'Andorra'), ('AO', 'Angola'), ('AI', 'Anguilla'), ('AQ', 'Antarctica'), ('AG', 'Antigua en Barbuda'), ('AR', 'Argentinië'), ('AM', 'Armenië'), ('AW', 'Aruba'), ('AU', 'Australië'), ('AT', 'Oostenrijk'), ('AZ', 'Azerbeidzjan'), ('BS', "Bahama's"), ('BH', 'Bahrein'), ('BD', 'Bangladesh'), ('BB', 'Barbados'), ('BY', 'Wit-Rusland / Belarus'), ('BE', 'België'), ('BZ', 'Belize'), ('BJ', 'Benin'), ('BM', 'Bermuda'), ('BT', 'Bhutan'), ('BO', 'Bolivia, Plurinationale Staat'), ('BQ', 'Bonaire, Sint Eustatius en Saba'), ('BA', 'Bosnië en Herzegovina'), ('BW', 'Botswana'), ('BV', 'Bouvet'), ('BR', 'Brazilië'), ('IO', 'Brits Territorium in de Indische Oceaan'), ('BN', 'Brunei'), ('BG', 'Bulgarije'), ('BF', 'Burkina Faso'), ('BI', 'Burundi'), ('KH', 'Cambodja'), ('CM', 'Kameroen'), ('CA', 'Canada'), ('CV', 'Kaap Verde'), ('KY', 'Kaaimaneilanden'), ('CF', 'Centraal-Afrikaanse Republiek'), ('TD', 'Tsjaad'), ('CL', 'Chili'), ('CN', 'China'), ('CX', 'Christmaseiland'), ('CC', 'Cocoseilanden'), ('CO', 'Colombia'), ('KM', 'Comoren'), ('CG', 'Congo-Brazzaville'), ('CD', 'Congo-Kinshasa'), ('CK', 'Cookeilanden'), ('CR', 'Costa Rica'), ('CI', 'Ivoorkust'), ('HR', 'Kroatië'), ('CU', 'Cuba'), ('CW', 'Curaçao'), ('CY', 'Cyprus'), ('CZ', 'Tsjechië'), ('DK', 'Denemarken'), ('DJ', 'Djibouti'), ('DM', 'Dominica'), ('DO', 'Dominicaanse Republiek'), ('EC', 'Ecuador'), ('EG', 'Egypte'), ('SV', 'El Salvador'), ('GQ', 'Equatoriaal-Guinea'), ('ER', 'Eritrea'), ('EE', 'Estland'), ('ET', 'Ethiopië'), ('FK', 'Falklandeilanden'), ('FO', 'Faeröer'), ('FJ', 'Fiji'), ('FI', 'Finland'), ('FR', 'Frankrijk'), ('GF', 'Frans-Guyana'), ('PF', 'Frans-Polynesië'), ('TF', 'Franse Zuidelijke en Antarctische Gebieden'), ('GA', 'Gabon'), ('GM', 'Gambia'), ('GE', 'Georgië'), ('DE', 'Duitsland'), ('GH', 'Ghana'), ('GI', 'Gibraltar'), ('GR', 'Griekenland'), ('GL', 'Groenland'), ('GD', 'Grenada'), ('GP', 'Guadeloupe'), ('GU', 'Guam'), ('GT', 'Guatemala'), ('GG', 'Guernsey'), ('GN', 'Guinee'), ('GW', 'Guinee-Bissau'), ('GY', 'Guyana'), ('HT', 'Haïti'), ('HM', 'Heardeiland en McDonaldeilanden'), ('VA', 'Vaticaanstad'), ('HN', 'Honduras'), ('HK', 'Hong Kong'), ('HU', 'Hongarije'), ('IS', 'IJsland'), ('IN', 'IndiaIndia'), ('ID', 'Indonesië'), ('IR', 'Iran'), ('IQ', 'Irak'), ('IE', 'Ierland'), ('IM', 'Man'), ('IL', 'Israël'), ('IT', 'Italië'), ('JM', 'Jamaica'), ('JP', 'Japan'), ('JE', 'Jersey'), ('JO', 'Jordanië'), ('KZ', 'Kazachstan'), ('KE', 'Kenia'), ('KI', 'KiribatiKiribati'), ('KP', 'Noord-Korea'), ('KR', 'Zuid-Korea'), ('KW', 'Koeweit'), ('KG', 'Kirgizië'), ('LA', 'Laos'), ('LV', 'Letland'), ('LB', 'Libanon'), ('LS', 'Lesotho'), ('LR', 'Liberia'), ('LY', 'Libië'), ('LI', 'Liechtenstein'), ('LT', 'Litouwen'), ('LU', 'Luxemburg'), ('MO', 'Macau'), ('MK', 'Macedonië'), ('MG', 'Madagaskar'), ('MW', 'Malawi'), ('MY', 'Maleisië'), ('MV', 'Maldiven'), ('ML', 'Mali'), ('MT', 'Malta'), ('MH', 'Marshalleilanden'), ('MQ', 'Martinique'), ('MR', 'Mauritanië'), ('MU', 'Mauritius'), ('YT', 'Mayotte'), ('MX', 'Mexico'), ('FM', 'Micronesië'), ('MD', 'Moldavië'), ('MC', 'Monaco'), ('MN', 'Mongolië'), ('ME', 'Montenegro'), ('MS', 'Montserrat'), ('MA', 'Marokko'), ('MZ', 'Mozambique'), ('MM', 'Myanmar'), ('NA', 'Namibië'), ('NR', 'Nauru'), ('NP', 'Nepal'), ('NL', 'Nederland'), ('NC', 'Nieuw-Caledonië'), ('NZ', 'Nieuw Zeeland'), ('NI', 'Nicaragua'), ('NE', 'Niger'), ('NG', 'Nigeria'), ('NU', 'Niue'), ('NF', 'Norfolk'), ('MP', 'Noordelijke Marianen'), ('NO', 'Noorwegen'), ('OM', 'Oman'), ('PK', 'Pakistan'), ('PW', 'Palau'), ('PS', 'Palestijnse Gebieden'), ('PA', 'Panama'), ('PG', 'Papoea-Nieuw-Guinea'), ('PY', 'Paraguay'), ('PE', 'Peru'), ('PH', 'Filipijnen'), ('PN', 'Pitcairneilanden'), ('PL', 'Polen'), ('PT', 'Portugal'), ('PR', 'Puerto Rico'), ('QA', 'Qatar'), ('RE', 'Réunion'), ('RO', 'Roemenië'), ('RU', 'Rusland'), ('RW', 'Rwanda'), ('BL', 'Saint-Barthélemy'), ('SH', 'Sint-Helena, Ascension en Tristan da Cunha'), ('KN', 'Saint Kitts en Nevis'), ('LC', 'Saint Lucia'), ('MF', 'Saint-Martin'), ('PM', 'Saint-Pierre en Miquelon'), ('VC', 'Saint Vincent en de Grenadines'), ('WS', 'Samoa'), ('SM', 'San Marino'), ('ST', 'Sao Tomé en Principe'), ('SA', 'Saoedi-Arabië'), ('SN', 'Senegal'), ('RS', 'Servië'), ('SC', 'Seychellen'), ('SL', 'Sierra Leone'), ('SG', 'Singapore'), ('SX', 'Sint Maarten'), ('SK', 'Slowakije'), ('SI', 'Slovenië'), ('SB', 'Salomonseilanden'), ('SO', 'Somalië'), ('ZA', 'Zuid Afrika'), ('GS', 'Zuid-Georgië en de Zuidelijke Sandwicheilanden'), ('ES', 'Spanje'), ('LK', 'Sri Lanka'), ('SD', 'Soedan'), ('SR', 'Suriname'), ('SJ', 'Spitsbergen en Jan Mayen'), ('SZ', 'Swaziland'), ('SE', 'Zweden'), ('CH', 'Zwitserland'), ('SY', 'Syrië'), ('TW', 'Taiwan'), ('TJ', 'Tadzjikistan'), ('TZ', 'Tanzania'), ('TH', 'Thailand'), ('TL', 'Oost-Timor'), ('TG', 'Togo'), ('TK', 'Tokelau-eilanden'), ('TO', 'Tonga'), ('TT', 'Trinidad en Tobago'), ('TN', 'Tunesië'), ('TR', 'Turkije'), ('TM', 'Turkmenistan'), ('TC', 'Turks- en Caicoseilanden'), ('TV', 'Tuvalu'), ('UG', 'Oeganda'), ('UA', 'Oekraïne'), ('AE', 'Verenigde Arabische Emiraten'), ('GB', 'Verenigd Koninkrijk'), ('US', 'Verenigde Staten'), ('UM', 'Kleine afgelegen eilanden van de Verenigde Staten'), ('UY', 'Uruguay'), ('UZ', 'Oezbekistan'), ('VU', 'Vanuatu'), ('VE', 'Venezuela'), ('VN', 'Vietnam'), ('VG', 'Maagdeneilanden, Brits'), ('VI', 'Maagdeneilanden, Amerikaans'), ('WF', 'Wallis en Futuna'), ('EH', 'Westelijke Sahara'), ('YE', 'Jemen'), ('ZM', 'Zambia'), ('ZW', 'Zimbabwe')], max_length=2, verbose_name='country')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='e-mail')),
                ('phone_fixed', models.CharField(blank=True, max_length=16, verbose_name='phone fixed')),
                ('machazine', models.BooleanField(default=True, verbose_name='MaCHazine')),
                ('board_invites', models.BooleanField(default=False, verbose_name='board invites')),
                ('constitution_card', models.BooleanField(default=False, verbose_name='constitution card')),
                ('christmas_card', models.BooleanField(default=True, verbose_name='Christmas card')),
                ('yearbook', models.BooleanField(default=False, verbose_name='yearbook')),
                ('comment', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'entity',
                'verbose_name_plural': 'entities',
            },
        ),
        migrations.CreateModel(
            name='Modification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='date')),
                ('ip', models.CharField(max_length=40, verbose_name='ip address')),
                ('modification', models.TextField(blank=True, verbose_name='modification')),
            ],
            options={
                'verbose_name': 'modification',
                'verbose_name_plural': 'modifications',
            },
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('entity_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='ldb.Entity')),
                ('name_prefix', models.CharField(max_length=100, verbose_name='name prefix')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('name_short', models.CharField(blank=True, max_length=100, verbose_name='name short')),
                ('salutation', models.CharField(max_length=100, verbose_name='salutation')),
            ],
            options={
                'verbose_name': 'organization',
                'verbose_name_plural': 'organizations',
            },
            bases=('ldb.entity',),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('entity_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='ldb.Entity')),
                ('titles', models.CharField(blank=True, max_length=20, verbose_name='titles')),
                ('initials', models.CharField(max_length=15, verbose_name='initials')),
                ('firstname', models.CharField(max_length=50, verbose_name='first name')),
                ('preposition', models.CharField(blank=True, max_length=15, verbose_name='preposition')),
                ('surname', models.CharField(max_length=100, verbose_name='surname')),
                ('postfix_titles', models.CharField(blank=True, max_length=20, verbose_name='postfix titles')),
                ('phone_mobile', models.CharField(blank=True, max_length=16, verbose_name='phone mobile')),
                ('gender', models.CharField(blank=True, choices=[(b'M', 'Male'), (b'F', 'Female')], max_length=1, verbose_name='gender')),
                ('birthdate', models.DateField(blank=True, null=True, verbose_name='birthdate')),
                ('deceased', models.BooleanField(default=False, verbose_name='deceased')),
                ('mail_announcements', models.BooleanField(default=True, verbose_name='announcements mailing')),
                ('mail_company', models.BooleanField(default=True, verbose_name='company mailing')),
                ('ldap_username', models.CharField(blank=True, max_length=50, verbose_name='LDAP username')),
                ('netid', models.CharField(blank=True, max_length=32, verbose_name='NetID')),
                ('linkedin_id', models.CharField(blank=True, max_length=32, verbose_name='LinkedIn ID')),
                ('facebook_id', models.CharField(blank=True, max_length=32, verbose_name='Facebook ID')),
            ],
            options={
                'verbose_name': 'person',
                'verbose_name_plural': 'people',
            },
            bases=('ldb.entity',),
        ),
        migrations.CreateModel(
            name='Alumnus',
            fields=[
                ('person', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='ldb.Person')),
                ('study', models.CharField(blank=True, max_length=100, verbose_name='study')),
                ('study_first_year', models.IntegerField(blank=True, null=True, verbose_name='study first year')),
                ('study_last_year', models.IntegerField(blank=True, null=True, verbose_name='study last year')),
                ('study_research_group', models.CharField(blank=True, max_length=100, verbose_name='research group')),
                ('study_paper', models.CharField(blank=True, max_length=300, verbose_name='paper')),
                ('study_professor', models.CharField(blank=True, max_length=100, verbose_name='professor')),
                ('work_company', models.CharField(blank=True, max_length=100, verbose_name='company')),
                ('work_position', models.CharField(blank=True, max_length=100, verbose_name='position')),
                ('work_sector', models.CharField(blank=True, max_length=100, verbose_name='sector')),
                ('contact_method', models.CharField(choices=[(b'm', b'Mail'), (b'e', b'Email')], default=b'e', max_length=1, verbose_name='contact method')),
            ],
            options={
                'verbose_name': 'alumnus',
                'verbose_name_plural': 'alumni',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('person', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='ldb.Person')),
                ('faculty', models.CharField(max_length=50, verbose_name='faculty')),
                ('department', models.CharField(max_length=50, verbose_name='department')),
                ('function', models.CharField(max_length=50, verbose_name='function')),
                ('phone_internal', models.CharField(max_length=5, verbose_name='phone internal')),
            ],
            options={
                'verbose_name': 'employee',
                'verbose_name_plural': 'employees',
            },
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('person', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='ldb.Person')),
                ('date_from', models.DateField(blank=True, null=True, verbose_name='date from')),
                ('date_to', models.DateField(blank=True, null=True, verbose_name='date to')),
                ('date_paid', models.DateField(blank=True, null=True, verbose_name='date paid')),
                ('amount_paid', models.IntegerField(blank=True, null=True, verbose_name='amount paid')),
                ('associate_member', models.BooleanField(default=False, verbose_name='associate member')),
                ('donating_member', models.BooleanField(default=False, verbose_name='donating member')),
                ('merit_date_from', models.DateField(blank=True, null=True, verbose_name='merit member date from')),
                ('merit_invitations', models.BooleanField(default=True, verbose_name='merit member invitations')),
                ('merit_history', models.TextField(blank=True, verbose_name='merit member history')),
                ('honorary_date_from', models.DateField(blank=True, null=True, verbose_name='honorary member from date')),
            ],
            options={
                'verbose_name': 'member',
                'verbose_name_plural': 'members',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('person', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='ldb.Person')),
                ('study', models.CharField(max_length=50, verbose_name='study')),
                ('first_year', models.IntegerField(blank=True, null=True, verbose_name='first year')),
                ('student_number', dienst2.extras.CharNullField(blank=True, max_length=7, null=True, verbose_name='student number')),
                ('graduated', models.BooleanField(default=False, verbose_name='graduated')),
                ('phone_parents', models.CharField(blank=True, max_length=16, verbose_name='phone parents')),
                ('yearbook_permission', models.BooleanField(default=True, verbose_name='yearbook permission')),
                ('date_verified', models.DateField(blank=True, null=True, verbose_name='date verified')),
            ],
            options={
                'verbose_name': 'student',
                'verbose_name_plural': 'students',
            },
        ),
        migrations.AddField(
            model_name='person',
            name='living_with',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ldb.Person'),
        ),
        migrations.AddField(
            model_name='modification',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ldb.Person'),
        ),
        migrations.AddField(
            model_name='committeemembership',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ldb.Person'),
        ),
        migrations.AddField(
            model_name='committee',
            name='members',
            field=models.ManyToManyField(through='ldb.CommitteeMembership', to='ldb.Person'),
        ),
        migrations.AlterField(
            model_name='person',
            name='facebook_id',
            field=dienst2.extras.CharNullField(blank=True, max_length=64, null=True, verbose_name='Facebook ID'),
        ),
        migrations.AlterField(
            model_name='person',
            name='ldap_username',
            field=dienst2.extras.CharNullField(blank=True, max_length=64, null=True, verbose_name='LDAP username'),
        ),
        migrations.AlterField(
            model_name='person',
            name='linkedin_id',
            field=dienst2.extras.CharNullField(blank=True, max_length=64, null=True, verbose_name='LinkedIn ID'),
        ),
        migrations.AlterField(
            model_name='person',
            name='netid',
            field=dienst2.extras.CharNullField(blank=True, max_length=64, null=True, verbose_name='NetID'),
        ),
        migrations.RunSQL(
            sql="UPDATE ldb_person SET ldap_username = NULL WHERE ldap_username = '';",
        ),
        migrations.RunSQL(
            sql="UPDATE ldb_person SET linkedin_id = NULL WHERE linkedin_id = '';",
        ),
        migrations.RunSQL(
            sql="UPDATE ldb_person SET netid = NULL WHERE netid = '';",
        ),
        migrations.RunSQL(
            sql="UPDATE ldb_person SET facebook_id = NULL WHERE facebook_id = '';",
        ),
        migrations.RunSQL(
            sql="UPDATE ldb_student SET student_number = NULL WHERE student_number = '' OR student_number = '0';",
        ),
        migrations.AlterField(
            model_name='person',
            name='facebook_id',
            field=dienst2.extras.CharNullField(blank=True, max_length=64, null=True, unique=True, verbose_name='Facebook ID'),
        ),
        migrations.AlterField(
            model_name='person',
            name='ldap_username',
            field=dienst2.extras.CharNullField(blank=True, max_length=64, null=True, unique=True, verbose_name='LDAP username'),
        ),
        migrations.AlterField(
            model_name='person',
            name='linkedin_id',
            field=dienst2.extras.CharNullField(blank=True, max_length=64, null=True, unique=True, verbose_name='LinkedIn ID'),
        ),
        migrations.AlterField(
            model_name='person',
            name='netid',
            field=dienst2.extras.CharNullField(blank=True, max_length=64, null=True, unique=True, verbose_name='NetID'),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_number',
            field=dienst2.extras.CharNullField(blank=True, max_length=7, null=True, unique=True, verbose_name='student number'),
        ),
        migrations.AlterField(
            model_name='committeemembership',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='committee_memberships', to='ldb.Person'),
        ),
        migrations.RunSQL(
            sql='CREATE INDEX ldb_person_ldap_username_upper ON ldb_person (UPPER(ldap_username));',
        ),
        migrations.RunSQL(
            sql='CREATE INDEX ldb_person_netid_upper ON ldb_person (UPPER(netid));',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='graduated',
            new_name='enrolled',
        ),
        migrations.AlterField(
            model_name='student',
            name='enrolled',
            field=models.BooleanField(default=True, verbose_name='enrolled'),
        ),
        migrations.RunSQL(
            sql='UPDATE ldb_student SET enrolled = NOT enrolled;',
        ),
        migrations.AddField(
            model_name='person',
            name='_membership_status',
            field=ldb.formTemplates.membershipStatusField.MembershipStatusField(db_column='membership_status', default=0, enum=ldb.formTemplates.membershipStatus.MembershipStatus),
        ),
        migrations.AddField(
            model_name='person',
            name='mail_education',
            field=models.BooleanField(default=True, verbose_name='education mailing'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='name_prefix',
            field=models.CharField(blank=True, max_length=100, verbose_name='name prefix'),
        ),
        migrations.AlterModelOptions(
            name='committee',
            options={'ordering': ['name'], 'verbose_name': 'committee', 'verbose_name_plural': 'committees'},
        ),
        migrations.AlterModelOptions(
            name='committeemembership',
            options={'ordering': ['board', 'committee__name'], 'verbose_name': 'committee membership', 'verbose_name_plural': 'committee memberships'},
        ),
        migrations.AlterField(
            model_name='alumnus',
            name='contact_method',
            field=models.CharField(choices=[('m', 'Mail'), ('e', 'Email')], default='e', max_length=1, verbose_name='contact method'),
        ),
        migrations.AlterField(
            model_name='person',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=1, verbose_name='gender'),
        ),
    ]

import faker

print(f"{faker.VERSION =}")

fake = faker.Faker()

print(
    f"""
    {fake.address()                 =}
    {fake.am_pm()                   =}
    {fake.android_platform_token()  =}
    {fake.ascii_company_email()     =}
    {fake.ascii_email()             =}
    {fake.ascii_free_email()        =}
    {fake.ascii_safe_email()        =}
    {fake.bank_country()            =}
    {fake.boolean()                 =}
    {fake.building_number()         =}
    #{fake.cache_pattern            =}
    {fake.catch_phrase()            =}
    {fake.century()                 =}
    {fake.chrome()                  =}
    {fake.city()                    =}
    {fake.city_prefix()             =}
    {fake.city_suffix()             =}
    {fake.color()                   =}
    {fake.color_name()              =}
    {fake.company()                 =}
    {fake.company_email()           =}
    {fake.company_suffix()          =}
    {fake.coordinate()              =}
    {fake.country()                 =}
    {fake.country_calling_code()    =}
    {fake.country_code()            =}
    {fake.credit_card_expire()      =}
    {fake.credit_card_full()        =}
    {fake.credit_card_number()      =}
    {fake.credit_card_provider()    =}
    {fake.credit_card_security_code()=}
    {fake.cryptocurrency()          =}
    {fake.cryptocurrency_code()     =}
    {fake.cryptocurrency_name()     =}
    {fake.csv()                     =}
    {fake.currency()                =}
    {fake.currency_code()           =}
    {fake.currency_name()           =}
    {fake.currency_symbol()         =}
    {fake.hex_color()               =}
    {fake.hexify()                  =}
    {fake.hostname()                =}
    {fake.http_method()             =}
    {fake.iana_id()                 =}
    {fake.image()                   =}
    {fake.image_url()               =}
    {fake.internet_explorer()       =}
    {fake.invalid_ssn()             =}
    {fake.ios_platform_token()      =}
    {fake.ipv4()                    =}
    {fake.ipv4_network_class()      =}
    {fake.ipv4_private()            =}
    {fake.ipv4_public()             =}
    {fake.ipv6()                    =}
    {fake.isbn10()                  =}
    {fake.isbn13()                  =}
    {fake.iso8601()                 =}
    {fake.json()                    =}
    {fake.language_code()           =}
    {fake.language_name()           =}
    {fake.last_name()               =}
    {fake.last_name_female()        =}
    {fake.last_name_male()          =}
    {fake.last_name_nonbinary()     =}
    {fake.latitude()                =}
    {fake.latlng()                  =}
    {fake.lexify()                  =}
    {fake.license_plate()           =}
    {fake.linux_platform_token()    =}
    {fake.linux_processor()         =}
    {fake.local_latlng()            =}

    {fake.unix_device()             =}
    {fake.unix_partition()          =}
    {fake.unix_time()               =}
    {fake.upc_a()                   =}
    {fake.upc_e()                   =}
    {fake.uri()                     =}
    {fake.uri_extension()           =}
    {fake.uri_page()                =}
    {fake.uri_path()                =}
    {fake.url()                     =}
    {fake.user_agent()              =}
    {fake.user_name()               =}
    {fake.uuid4()                   =}
    {fake.weights                   =}
    {fake.windows_platform_token()  =}
    {fake.word()                    =}
    {fake.words()                   =}
    {fake.year()                    =}
    {fake.zipcode()                 =}
    {fake.zipcode_in_state()        =}
    {fake.zipcode_plus4()           =}


"""
)

# 'aba', 'add_provider',
# 'administrative_unit',
# 'bban', 'bothify', 'bs', 'binary'
# 'current_couarguments',
#  'get_formatter',
# 'get_providers',
#  'iban', 'itin', items()
#  'job',
# 'locale', 'locales', 'localized_ean', 'localized_ean13',
#  'localized_ean8', 'location_on_land',
#  'longitude', 'mac_address', 'mac_platform_token',
#  'mac_processor', 'md5', 'military_apo', 'military_dpo',
#  'military_ship', 'military_state', 'mime_type', 'month',
# 'month_name', 'msisdn', 'name', 'name_female', 'name_male',
#  'name_nonbinary', 'nic_handle', 'nic_handles', 'null_boolean',
# 'numerify', 'opera', 'paragraph', 'paragraphs', 'parse',
# 'password', 'past_date', 'past_datetime', 'phone_number',
# 'port_number', 'postalcode', 'postalcode_in_state',
# 'postalcode_plus4', 'postcode', 'postcode_in_state', 'prefix',
#  'prefix_female', 'prefix_male', 'prefix_nonbinary', 'pricetag',
#  'profile', 'provider', 'providers', 'psv', 'pybool', 'pydecimal',
#  'pydict', 'pyfloat', 'pyint', 'pyiterable', 'pylist', 'pyset',
# 'pystr', 'pystr_format', 'pystruct', 'pytimezone', 'pytuple', 'random',
#  'random_choices', 'random_digit', 'random_digit_not_null',
#  'random_digit_not_null_or_empty', 'random_digit_or_empty',
# 'random_element', 'random_elements', 'random_int', 'random_letter',
#  'random_letters', 'random_lowercase_letter', 'random_number',
# 'random_sample', 'random_uppercase_letter', 'randomize_nb_elements',
#  'rgb_color', 'rgb_css_color', 'ripe_id', 'safari', 'safe_color_name',
#  'safe_domain_name', 'safe_email', 'safe_hex_color', 'secondary_address',
#  'seed', 'seed_instance', 'seed_locale', 'sentence', 'sentences',
# 'set_arguments', 'set_formatter', 'sha1', 'sha256', 'simple_profile',
# 'slug', 'ssn', 'state', 'state_abbr', 'street_address', 'street_name',
# 'street_suffix', 'suffix', 'suffix_female', 'suffix_male', 'suffix_nonbinary',
#  'swift', 'swift11', 'swift8', 'tar', 'text', 'texts', 'time', 'time_delta',
# 'time_object', 'time_series', 'timezone', 'tld', 'tsv', 'unique'
# zip()

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
import uuid
from django.utils import timezone

class AllowCities(models.Model):
    allow_state_id = models.IntegerField(blank=True, null=True)
    city_name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'allow_cities'


class AllowCountries(models.Model):
    country_id = models.IntegerField(blank=True, null=True)
    country_name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'allow_countries'


class AllowStates(models.Model):
    country_id = models.IntegerField(blank=True, null=True)
    allow_country_id = models.CharField(max_length=255, blank=True, null=True)
    state_name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'allow_states'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class AwardCouponHistories(models.Model):
    id = models.CharField(primary_key=True, max_length=30, db_column='pk')
    customer_id = models.CharField(max_length=30, blank=True, null=True)
    award_coupon_id = models.CharField(max_length=30, blank=True, null=True)
    award_coupon_code = models.CharField(max_length=30, blank=True, null=True)
    award_name = models.CharField(max_length=30, blank=True, null=True)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'award_coupon_histories'


class AwardCouponInfos(models.Model):
    # pk = models.CharField(primary_key=True, max_length=30)
    vendor_id = models.CharField(max_length=40, blank=True, null=True)
    coupon_name = models.CharField(max_length=255, blank=True, null=True)
    coupon_code = models.CharField(max_length=50)
    award_name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    uses_total = models.IntegerField(blank=True, null=True)
    uses_customer = models.IntegerField(blank=True, null=True)
    date_start = models.DateField(blank=True, null=True)
    date_end = models.DateField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    discard = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'award_coupon_infos'


class BookingClasses(models.Model):
    id = models.CharField(default=uuid.uuid4, primary_key=True, unique=True, max_length=40, db_column = 'pk')
    date_added = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    class_name = models.CharField(max_length=255, blank=True, null=True)
    vendor_id = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    age_min = models.IntegerField(blank=True, null=True)
    age_max = models.IntegerField(blank=True, null=True)
    cover_image = models.CharField(max_length=255, blank=True, null=True)
    image_list = models.CharField(max_length=255, blank=True, null=True)
    youtube_code = models.CharField(max_length=255, blank=True, null=True)
    teaching_type_1 = models.IntegerField(blank=True, null=True)
    teaching_type_2 = models.IntegerField(blank=True, null=True)
    teaching_type_3 = models.IntegerField(blank=True, null=True)
    teaching_type_4 = models.IntegerField(blank=True, null=True)
    teaching_type_5 = models.IntegerField(blank=True, null=True)
    teaching_type_6 = models.IntegerField(blank=True, null=True)
    teaching_type_7 = models.IntegerField(blank=True, null=True)
    teaching_type_8 = models.IntegerField(blank=True, null=True)
    comment_status = models.IntegerField(blank=True, null=True)
    view_count = models.IntegerField(blank=True, null=True)
    ad_paid = models.IntegerField(blank=True, null=True)
    transaction_item_id = models.CharField(max_length=30)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.date_added = timezone.now()
        super(BookingClasses, self).save(*args, **kwargs)

    class Meta:
        managed = False
        db_table = 'booking_classes'


class BookingSchoolCoupons(models.Model):
    # pk = models.CharFi/eld(primary_key=True, max_length=30)
    school_coupon_name = models.CharField(max_length=128)
    school_coupon_code = models.CharField(max_length=20)
    school_discount_minus = models.DecimalField(max_digits=15, decimal_places=4, blank=True, null=True)
    school_discount_percent = models.DecimalField(max_digits=15, decimal_places=4, blank=True, null=True)
    transaction_fee = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    total = models.DecimalField(max_digits=15, decimal_places=4, blank=True, null=True)
    date_start = models.DateField(blank=True, null=True)
    date_end = models.DateField(blank=True, null=True)
    uses_total = models.IntegerField(blank=True, null=True)
    uses_customer = models.IntegerField(blank=True, null=True)
    each_customer_quota = models.IntegerField(blank=True, null=True)
    each_customer_per_vendor_quota = models.IntegerField(blank=True, null=True)
    each_customer_amount = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    date_added = models.DateTimeField(blank=True, null=True)
    vendor_id = models.CharField(max_length=255, blank=True, null=True)
    price_prefix = models.CharField(max_length=3)
    companion = models.IntegerField(blank=True, null=True)
    transaction_item_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'booking_school_coupons'


class BranchHistories(models.Model):
    id = models.CharField(default = uuid.uuid4, primary_key=True, unique=True, max_length=40, db_column='pk')
    date_added = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    class_branch = models.CharField(max_length=255)
    class_id = models.CharField(max_length=255)
    country = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    booking_class_id = models.CharField(max_length=40)

    def save(self, *args, **kwargs):
        self.date_added = timezone.now()
        super(BranchHistories, self).save(*args, **kwargs)

    class Meta:
        managed = False
        db_table = 'branch_histories'


class ClassBranches(models.Model):
    id = models.CharField(primary_key=True, unique=True, max_length=40, db_column='pk')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    class_branch = models.CharField(max_length=255)
    classes = models.ForeignKey('VendorClasses', related_name='class_branches', to_field='id', on_delete=models.DO_NOTHING, db_constraint=False, db_column='class_id')
    country = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    district = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    enable_date = models.DateTimeField(blank=True, null=True)
    disable_date = models.DateTimeField(blank=True, null=True)
    preview_date = models.DateTimeField(blank=True, null=True)
    branch_id = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'class_branches'


class ClassCategories(models.Model):
    # pk = models.CharField(unique=True, max_length=40, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    class_id = models.CharField(max_length=255)
    category_name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'class_categories'


class ClassComments(models.Model):
    # pk = models.CharField(unique=True, max_length=30)
    class_history_id = models.CharField(max_length=40, blank=True, null=True)
    class_name = models.CharField(max_length=255, blank=True, null=True)
    vendor_id = models.CharField(max_length=255, blank=True, null=True)
    star = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'class_comments'


class ClassOptions(models.Model):
    id = models.CharField(primary_key=True, unique=True, max_length=40, db_column='pk')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    branch = models.ForeignKey('ClassBranches', related_name='class_branches', to_field='id', on_delete=models.DO_NOTHING, db_constraint=False)
    option_name = models.CharField(max_length=255)
    option_formula = models.TextField(blank=True, null=True)
    subtract = models.IntegerField(blank=True, null=True)
    currency_id = models.IntegerField(blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    price_prefix = models.CharField(max_length=5, blank=True, null=True)
    points = models.IntegerField(blank=True, null=True)
    points_prefix = models.CharField(max_length=5, blank=True, null=True)
    need_register_fee = models.IntegerField()
    ecredit_rate = models.IntegerField()
    auto_renew_status = models.IntegerField(blank=True, null=True)
    schedule_free_status = models.IntegerField(blank=True, null=True)
    best_discount_price = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    best_discount_match = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'class_options'


class ClassPages(models.Model):
    # pk = models.CharField(primary_key=True, max_length=40)
    template_id = models.CharField(max_length=40, blank=True, null=True)
    class_id = models.CharField(max_length=40, blank=True, null=True)
    page_type = models.CharField(max_length=7)
    page_text = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'class_pages'


class ClassSchedules(models.Model):
    id = models.CharField(primary_key=True, unique=True, max_length=40, db_column='pk')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    option = models.ForeignKey('ClassOptions', related_name='class_schedules', to_field='id', on_delete=models.DO_NOTHING, db_constraint=False, null=True, db_column='option_id')
    schedule_name = models.CharField(max_length=255)
    next_term_id = models.CharField(max_length=80, blank=True, null=True)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    start_time = models.CharField(max_length=255, blank=True, null=True)
    end_time = models.CharField(max_length=255, blank=True, null=True)
    vacancy = models.IntegerField(blank=True, null=True)
    capacity = models.IntegerField(blank=True, null=True)

    

    class Meta:
        managed = False
        db_table = 'class_schedules'


class ClassScoreLogs(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    class_id = models.CharField(max_length=255)
    score_source = models.CharField(max_length=255, blank=True, null=True)
    score_data = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'class_score_logs'


class ClassViewLogs(models.Model):
    # pk = models.CharField(unique=True, max_length=40, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    class_id = models.CharField(max_length=255)
    device_id = models.CharField(max_length=255, blank=True, null=True)
    device_type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'class_view_logs'


class CommentHistories(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    customer_name = models.CharField(max_length=64)
    comment_type = models.CharField(max_length=32)
    email = models.CharField(max_length=96)
    comment = models.TextField()

    class Meta:
        managed = False
        db_table = 'comment_histories'

class CoreBauser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()
    eda_role = models.CharField(max_length=512, blank=True, null=True)
    lej_api_token = models.CharField(max_length=2048, blank=True, null=True)
    reverse_token = models.CharField(max_length=2048, blank=True, null=True)
    password_raw = models.CharField(max_length=255, blank=True, null=True)
    tb_api_token = models.CharField(max_length=2048, blank=True, null=True)
    ms_api_token = models.CharField(max_length=2048, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'core_bauser'


class CountryHolidays(models.Model):
    # id = models.CharField(primary_key=True, max_length=40, db_column = 'pk')
    holiday_name = models.CharField(max_length=40, blank=True, null=True)
    holiday_date = models.DateField(blank=True, null=True)
    country_code = models.CharField(max_length=2, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'country_holidays'


class CountryLists(models.Model):
    id = models.AutoField(primary_key=True, db_column= 'pk')
    country_code = models.CharField(max_length=2)
    country_code_alpha3 = models.CharField(max_length=3, blank=True, null=True)
    country_code_num = models.CharField(max_length=3, blank=True, null=True)
    currency_code = models.CharField(max_length=3, blank=True, null=True)
    country_name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'country_lists'


class CouponRuleInfos(models.Model):
    # pk = models.AutoField(primary_key=True)
    rule_name = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'coupon_rule_infos'


class CurrencyLists(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    currency_code = models.CharField(max_length=15)
    currency_name = models.CharField(max_length=255, blank=True, null=True)
    country_id = models.IntegerField(blank=True, null=True)
    exchange_rate = models.DecimalField(max_digits=20, decimal_places=6, blank=True, null=True)
    ecredit_rate = models.DecimalField(max_digits=20, decimal_places=6, blank=True, null=True)
    allow_payment = models.IntegerField(blank=True, null=True)
    stripe_rule = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'currency_lists'


class CustomerActivities(models.Model):
    idno = models.AutoField(primary_key=True)
    method = models.CharField(max_length=10)
    path = models.TextField(blank=True, null=True)
    url = models.TextField()
    controller_name = models.CharField(max_length=1000)
    route_name = models.CharField(max_length=100)
    data = models.TextField()
    ip = models.CharField(max_length=50)
    request_time = models.DateTimeField()
    login_info = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer_activities'


class CustomerInfos(models.Model):
    id = models.CharField(default=str(uuid.uuid4())[0:30], primary_key=True, unique=True, max_length=40, db_column='pk')
    customer_id = models.CharField(max_length=30, blank=True, null=True)
    customer_group_id = models.IntegerField(blank=True, null=True)
    signup_group_id = models.IntegerField(blank=True, null=True)
    app_id = models.IntegerField(blank=True, null=True)
    customer_prefix = models.CharField(max_length=10, blank=True, null=True)
    customer_firstname = models.CharField(max_length=32, blank=True, null=True)
    customer_lastname = models.CharField(max_length=32, blank=True, null=True)
    customer_email = models.CharField(max_length=96, blank=True, null=True)
    customer_cc_email = models.CharField(max_length=96, blank=True, null=True)
    customer_telephone = models.CharField(max_length=32, blank=True, null=True)
    customer_mobile = models.CharField(max_length=32, blank=True, null=True)
    customer_password = models.CharField(max_length=80, blank=True, null=True)
    hashed_password = models.CharField(max_length=191)
    city = models.CharField(max_length=128, blank=True, null=True)
    country = models.CharField(max_length=128, blank=True, null=True)
    signup_country = models.CharField(max_length=128, blank=True, null=True)
    preferred_payment_mode = models.TextField(blank=True, null=True)
    cart = models.TextField(blank=True, null=True)
    newsletter = models.IntegerField(blank=True, null=True)
    customer_status = models.IntegerField(blank=True, null=True)
    customer_approved = models.IntegerField(blank=True, null=True)
    customer_code = models.CharField(max_length=40, blank=True, null=True)
    date_added = models.DateTimeField(blank=True, null=True)
    customer_email_status = models.IntegerField(blank=True, null=True)
    customer_welcome_status = models.IntegerField()
    upline_customer_id = models.CharField(max_length=40, blank=True, null=True)
    stripe_customer_id = models.CharField(max_length=50, blank=True, null=True)
    last_payment_at = models.DateTimeField(blank=True, null=True)
    device_type = models.IntegerField(blank=True, null=True)
    device_token = models.CharField(max_length=255, blank=True, null=True)
    device_gcm_badge = models.IntegerField(blank=True, null=True)
    image_url = models.CharField(max_length=255, blank=True, null=True)
    default_age = models.IntegerField(blank=True, null=True)
    ta_token = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer_infos'

class CustomerTokens(models.Model):
    lej_customer_id = models.CharField(max_length=30, blank=True, null=True)
    service_customer_id = models.CharField(max_length=50, blank=True, null=True)
    newebpay_authorized_token = models.CharField(max_length=255, blank=True, null=True)
    newebpay_authorized_token_life = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super(CustomerTokens, self).save(*args, **kwargs)
    class Meta:
        managed = True
        db_table = 'customer_tokens'


class CustomerLearningPlans(models.Model):
    # pk = models.CharField(unique=True, max_length=40, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    profile_id = models.CharField(max_length=30, blank=True, null=True)
    plan_keyword = models.CharField(max_length=255, blank=True, null=True)
    plan_icon = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer_learning_plans'


class CustomerLogins(models.Model):
    # pk = models.CharField(unique=True, max_length=30, blank=True, null=True)
    ip = models.CharField(max_length=40, blank=True, null=True)
    customer_id = models.CharField(max_length=40, blank=True, null=True)
    app_id = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    referer = models.TextField(blank=True, null=True)
    date_added = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer_logins'


class CustomerProfiles(models.Model):
    # pk = models.CharField(primary_key=True, max_length=30)
    customer_id = models.CharField(max_length=30, blank=True, null=True)
    app_id = models.IntegerField(blank=True, null=True)
    profile_firstname = models.CharField(max_length=32, blank=True, null=True)
    profile_lastname = models.CharField(max_length=32, blank=True, null=True)
    profile_dob = models.DateField(blank=True, null=True)
    profile_occupation = models.TextField(blank=True, null=True)
    profile_school = models.TextField(blank=True, null=True)
    image_cover_url = models.CharField(max_length=255, blank=True, null=True)
    image_url = models.CharField(max_length=255, blank=True, null=True)
    date_added = models.DateTimeField(blank=True, null=True)
    profile_gender = models.IntegerField(blank=True, null=True)
    date_updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer_profiles'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class EcreditHistories(models.Model):
    id = models.CharField(default=str(uuid.uuid4())[0:30], primary_key=True, max_length=30, db_column='pk')
    customer_id = models.CharField(max_length=30)
    change_date = models.DateField()
    date_added = models.DateTimeField(blank=True, null=True)
    change_point = models.PositiveIntegerField()
    add_minus = models.CharField(max_length=1)
    description = models.CharField(max_length=255, blank=True, null=True)
    price_prefix = models.CharField(max_length=5, blank=True, null=True)
    transaction_id = models.CharField(max_length=40, blank=True, null=True)
    
    def save(self, *args, **kwargs):
        self.change_date = timezone.now().date()
        self.date_added = timezone.now()
        super(EcreditHistories, self).save(*args, **kwargs)
    class Meta:
        managed = False
        db_table = 'ecredit_histories'


class EcreditsInviteInfos(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    invite_description = models.CharField(max_length=255, blank=True, null=True)
    invite_ecredits_point = models.DecimalField(max_digits=15, decimal_places=4, blank=True, null=True)
    invite_country = models.CharField(max_length=128, blank=True, null=True)
    invite_code = models.CharField(max_length=255, blank=True, null=True)
    invite_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ecredits_invite_infos'


class EcreditsRedeemHistories(models.Model):
    # pk = models.CharField(primary_key=True, max_length=30)
    customer_id = models.CharField(max_length=30)
    ecredits_redeem_id = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ecredits_redeem_histories'


class EcreditsRedeemInfos(models.Model):
    # pk = models.CharField(primary_key=True, max_length=30)
    redeem_name = models.CharField(max_length=128)
    redeem_code = models.CharField(max_length=15)
    redeem_description = models.CharField(max_length=255, blank=True, null=True)
    redeem_ecredits_point = models.DecimalField(max_digits=15, decimal_places=4, blank=True, null=True)
    redeem_price_prefix = models.CharField(max_length=3)
    redeem_use_total = models.IntegerField(blank=True, null=True)
    redeem_use_customer = models.IntegerField(blank=True, null=True)
    redeem_group_id = models.CharField(max_length=255, blank=True, null=True)
    redeem_date_start = models.DateField(blank=True, null=True)
    redeem_date_end = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ecredits_redeem_infos'


class EtbAdminInfos(models.Model):
    # pk = models.CharField(unique=True, max_length=40, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    admin_email = models.CharField(max_length=255)
    admin_account = models.CharField(max_length=255, blank=True, null=True)
    admin_password = models.CharField(max_length=255, blank=True, null=True)
    admin_hashed_password = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'etb_admin_infos'


class EtbUsers(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    # pk = models.CharField(max_length=40, blank=True, null=True)
    relation_table = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'etb_users'


class FailedJobs(models.Model):
    id = models.BigAutoField(primary_key=True)
    connection = models.TextField()
    queue = models.TextField()
    payload = models.TextField()
    exception = models.TextField()
    failed_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'failed_jobs'


class GuestInfos(models.Model):
    id = models.CharField(default=uuid.uuid4, primary_key=True, unique=True, max_length=255)
    email = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    mobile = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    
    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        self.created_at = timezone.now()
        super(GuestInfos, self).save(*args, **kwargs)


    class Meta:
        managed = False
        db_table = 'guest_infos'


class GuestTemporaryInfo(models.Model):
    id = models.CharField(default='aaaaaa', primary_key=True, unique=True, max_length=255)
    email = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    mobile = models.CharField(max_length=255)
    learners = models.CharField(max_length=255)
    schedule_id = models.CharField(max_length=255)
    auto_create_account = models.BooleanField(default=False)
    created_at = models.DateTimeField(blank=True, null=True)
    guest_id = models.CharField(max_length=255, blank=True, null=True)
    line_id = models.CharField(max_length=255, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.created_at = timezone.now()
        super(GuestTemporaryInfo, self).save(*args, **kwargs)


    class Meta:
        managed = True
        db_table = 'guest_temp_infos'


class Jobs(models.Model):
    id = models.BigAutoField(primary_key=True)
    queue = models.CharField(max_length=255)
    payload = models.TextField()
    attempts = models.PositiveIntegerField()
    reserved_at = models.PositiveIntegerField(blank=True, null=True)
    available_at = models.PositiveIntegerField()
    created_at = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'jobs'


class LejCategories(models.Model):
    # pk = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    category_name = models.CharField(max_length=255, blank=True, null=True)
    category_description = models.CharField(max_length=255, blank=True, null=True)
    display_order = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lej_categories'


class LejCouponCountry(models.Model):
    # pk = models.CharField(primary_key=True, max_length=30)
    lej_coupon_id = models.CharField(max_length=30)
    country_id = models.CharField(max_length=40)
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'lej_coupon_country'


class LejCouponCustomer(models.Model):
    # pk = models.CharField(primary_key=True, max_length=30)
    lej_coupon_id = models.CharField(max_length=30, blank=True, null=True)
    customer_id = models.CharField(max_length=30, blank=True, null=True)
    quota = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'lej_coupon_customer'


class LejCouponHistories(models.Model):
    # pk = models.CharField(primary_key=True, max_length=30)
    lej_coupon_id = models.CharField(max_length=30)
    transaction_id = models.CharField(max_length=30)
    customer_id = models.CharField(max_length=30)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    date_added = models.DateTimeField()
    description = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'lej_coupon_histories'


class LejCouponInfos(models.Model):
    # pk = models.CharField(primary_key=True, max_length=30)
    lej_coupon_name = models.CharField(max_length=128)
    lej_coupon_code = models.CharField(max_length=20)
    lej_discount_minus = models.DecimalField(max_digits=15, decimal_places=4, blank=True, null=True)
    lej_discount_percent = models.DecimalField(max_digits=15, decimal_places=4, blank=True, null=True)
    transaction_fee = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    total = models.DecimalField(max_digits=15, decimal_places=4, blank=True, null=True)
    date_start = models.DateField(blank=True, null=True)
    date_end = models.DateField(blank=True, null=True)
    uses_total = models.IntegerField(blank=True, null=True)
    uses_customer = models.IntegerField(blank=True, null=True)
    each_customer_quota = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    date_added = models.DateTimeField(blank=True, null=True)
    price_prefix = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'lej_coupon_infos'


class LejCouponVendor(models.Model):
    # pk = models.CharField(primary_key=True, max_length=30)
    lej_coupon_id = models.CharField(max_length=30)
    vendor_id = models.CharField(max_length=40)
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'lej_coupon_vendor'


class LejDiscounts(models.Model):
    # pk = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    discount_name = models.CharField(max_length=255, blank=True, null=True)
    discount_description = models.CharField(max_length=255, blank=True, null=True)
    display_order = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lej_discounts'


class MerchandiseOption1(models.Model):
    # pk = models.CharField(unique=True, max_length=40, blank=True, null=True)
    merchandise_id = models.CharField(max_length=30, blank=True, null=True)
    option_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'merchandise_option_1'


class MerchandiseOption2(models.Model):
    # pk = models.CharField(unique=True, max_length=40, blank=True, null=True)
    merchandise_id = models.CharField(max_length=30, blank=True, null=True)
    option_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'merchandise_option_2'


class Migrations(models.Model):
    migration = models.CharField(max_length=255)
    batch = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'migrations'


class NotificationHistories(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    date_send = models.DateTimeField(blank=True, null=True)
    target = models.CharField(max_length=255, blank=True, null=True)
    data = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notification_histories'


class OauthAccessTokens(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    user_id = models.IntegerField(blank=True, null=True)
    client_id = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    scopes = models.TextField(blank=True, null=True)
    revoked = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    expires_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oauth_access_tokens'


class OauthAuthCodes(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    user_id = models.IntegerField()
    client_id = models.IntegerField()
    scopes = models.TextField(blank=True, null=True)
    revoked = models.IntegerField()
    expires_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oauth_auth_codes'


class OauthClients(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255)
    secret = models.CharField(max_length=100)
    redirect = models.TextField()
    personal_access_client = models.IntegerField()
    password_client = models.IntegerField()
    revoked = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oauth_clients'


class OauthPersonalAccessClients(models.Model):
    client_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oauth_personal_access_clients'


class OauthRefreshTokens(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    access_token_id = models.CharField(max_length=100)
    revoked = models.IntegerField()
    expires_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oauth_refresh_tokens'


class OptionTypes(models.Model):
    # pk = models.CharField(primary_key=True, max_length=90)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    option_id = models.CharField(max_length=40, blank=True, null=True)
    type_id = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'option_types'


class ProfilingAnswers(models.Model):
    # pk = models.AutoField(primary_key=True)
    answer_type = models.IntegerField(blank=True, null=True)
    answer_content = models.TextField(blank=True, null=True)
    answer_age_min = models.IntegerField(blank=True, null=True)
    answer_age_max = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'profiling_answers'


class ProfilingLogs(models.Model):
    # pk = models.CharField(primary_key=True, max_length=30)
    profile_id = models.CharField(max_length=30, blank=True, null=True)
    type_1 = models.IntegerField(blank=True, null=True)
    type_2 = models.IntegerField(blank=True, null=True)
    type_3 = models.IntegerField(blank=True, null=True)
    type_4 = models.IntegerField(blank=True, null=True)
    type_5 = models.IntegerField(blank=True, null=True)
    type_6 = models.IntegerField(blank=True, null=True)
    type_7 = models.IntegerField(blank=True, null=True)
    type_8 = models.IntegerField(blank=True, null=True)
    date_added = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'profiling_logs'


class PromotionHistories(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    date_send = models.DateTimeField(blank=True, null=True)
    special_rule = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'promotion_histories'


class QueryLogs(models.Model):
    idno = models.AutoField(primary_key=True)
    method = models.CharField(max_length=20, blank=True, null=True)
    tb_name = models.CharField(max_length=30, blank=True, null=True)
    tb_pk = models.TextField(blank=True, null=True)
    data = models.TextField(blank=True, null=True)
    datetime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'query_logs'


class RedemptionHistories(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    notify_code = models.CharField(max_length=32)
    customer_id = models.CharField(unique=True, max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'redemption_histories'


class SchoolCouponBranch(models.Model):
    # pk = models.CharField(primary_key=True, max_length=30)
    school_coupon_id = models.CharField(max_length=30)
    branch_id = models.CharField(max_length=40)
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'school_coupon_branch'


class SchoolCouponClass(models.Model):
    # pk = models.CharField(primary_key=True, max_length=30)
    school_coupon_id = models.CharField(max_length=30)
    class_id = models.CharField(max_length=40)
    date_added = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'school_coupon_class'


class SchoolCouponCustomer(models.Model):
    id = models.CharField(primary_key=True, max_length=30, db_column='pk')
    school_coupon_id = models.CharField(max_length=30, blank=True, null=True)
    customer_id = models.CharField(max_length=30, blank=True, null=True)
    quota = models.IntegerField()
    date_end = models.DateField(blank=True, null=True)
    date_added = models.DateTimeField(blank=True, null=True)
    date_start = models.DateField(blank=True, null=True)
    valid_days = models.IntegerField(blank=True, null=True)
    date_updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'school_coupon_customer'


class SchoolCouponHistories(models.Model):
    # pk = models.CharField(primary_key=True, max_length=30)
    school_coupon_id = models.CharField(max_length=30)
    transaction_item_id = models.CharField(max_length=30)
    customer_id = models.CharField(max_length=30)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    date_added = models.DateTimeField()
    description = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'school_coupon_histories'


class SchoolCouponInfos(models.Model):
    id = models.CharField(primary_key=True, unique=True, max_length=30, db_column='pk')
    school_coupon_name = models.CharField(max_length=128)
    school_coupon_code = models.CharField(max_length=20)
    school_discount_minus = models.DecimalField(max_digits=15, decimal_places=4, blank=True, null=True)
    school_discount_percent = models.DecimalField(max_digits=15, decimal_places=4, blank=True, null=True)
    school_discount_minus2 = models.DecimalField(max_digits=15, decimal_places=4, blank=True, null=True)
    school_discount_percent2 = models.DecimalField(max_digits=15, decimal_places=4, blank=True, null=True)
    transaction_fee = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    total = models.DecimalField(max_digits=15, decimal_places=4, blank=True, null=True)
    date_start = models.DateField(blank=True, null=True)
    date_end = models.DateField(blank=True, null=True)
    uses_total = models.IntegerField(blank=True, null=True)
    uses_customer = models.IntegerField(blank=True, null=True)
    each_customer_quota = models.IntegerField(blank=True, null=True)
    each_customer_per_vendor_quota = models.IntegerField(blank=True, null=True)
    each_customer_amount = models.IntegerField(blank=True, null=True)
    topex_amount = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    date_added = models.DateTimeField(blank=True, null=True)
    vendor_id = models.CharField(max_length=255, blank=True, null=True)
    price_prefix = models.CharField(max_length=3)
    companion = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'school_coupon_infos'


class SchoolCouponLogs(models.Model):
    idno = models.AutoField(primary_key=True)
    method = models.CharField(max_length=20, blank=True, null=True)
    vendor_id = models.CharField(max_length=40, blank=True, null=True)
    tb_pk = models.TextField(blank=True, null=True)
    data = models.TextField(blank=True, null=True)
    datetime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'school_coupon_logs'


class SchoolCouponRules(models.Model):
    # pk = models.CharField(primary_key=True, max_length=30)
    school_coupon_id = models.CharField(max_length=30, blank=True, null=True)
    rule_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'school_coupon_rules'


class ScrapbookItems(models.Model):
    # pk = models.CharField(unique=True, max_length=40, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    type = models.IntegerField()
    url = models.CharField(max_length=255, blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    comment_date = models.DateTimeField(blank=True, null=True)
    rank = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    a = models.FloatField()
    b = models.FloatField()
    c = models.FloatField()
    d = models.FloatField()
    tx = models.FloatField()
    ty = models.FloatField()
    scrapbook_id = models.CharField(max_length=40)
    index = models.IntegerField()
    url_protected = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'scrapbook_items'


class Scrapbooks(models.Model):
    # pk = models.CharField(unique=True, max_length=40, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    class_name = models.CharField(max_length=255)
    vendor_name = models.CharField(max_length=255)
    type = models.IntegerField()
    customer_profile_id = models.CharField(max_length=30)
    booking_class_id = models.CharField(max_length=30, blank=True, null=True)
    vendor_class_id = models.CharField(max_length=255, blank=True, null=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    background_url = models.CharField(max_length=255, blank=True, null=True)
    canvas_width = models.FloatField(blank=True, null=True)
    canvas_height = models.FloatField(blank=True, null=True)
    device_type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'scrapbooks'


class ShoppingCarts(models.Model):
    id = models.CharField(default=str(uuid.uuid4())[0:20], primary_key=True, unique=True, max_length=40, db_column='pk')
    customer_id = models.CharField(max_length=40)
    schedule_id = models.CharField(max_length=40)
    coupon_id = models.CharField(max_length=40, blank=True, null=True)
    coupon_amount = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    subtotal = models.DecimalField(max_digits=15, decimal_places=2)
    special_note = models.TextField(blank=True, null=True)
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()
    type_id = models.CharField(max_length=40, blank=True, null=True)
    filter = models.TextField(blank=True, null=True)
    shoppingcart_summary_id = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shopping_carts'


class ShoppingcartMerchandises(models.Model):
    # pk = models.CharField(unique=True, max_length=40, blank=True, null=True)
    shoppingcart_id = models.CharField(max_length=40, blank=True, null=True)
    merchandise_id = models.CharField(max_length=40, blank=True, null=True)
    option1_id = models.CharField(max_length=40, blank=True, null=True)
    option2_id = models.CharField(max_length=40, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    date_added = models.DateTimeField(blank=True, null=True)
    shoppingcart_summary_id = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shoppingcart_merchandises'


class ShoppingcartProfiles(models.Model):
    id = models.CharField(default=str(uuid.uuid4())[0:20], primary_key=True, unique=True, max_length=40, db_column='pk')
    shoppingcart_id = models.CharField(max_length=40)
    profile_id = models.CharField(max_length=40, blank=True, null=True)
    profile_name = models.CharField(max_length=40)
    profile_dob = models.DateField()
    profile_note = models.CharField(max_length=255, blank=True, null=True)
    date_added = models.DateTimeField()
    image_url = models.CharField(max_length=255, blank=True, null=True)
    registration_fee = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'shoppingcart_profiles'


class ShoppingcartSummaries(models.Model):
    id = models.CharField(default=str(uuid.uuid4())[0:20], primary_key=True, unique=True, max_length=40, db_column='pk')
    customer_id = models.CharField(max_length=30)
    used_ecredits = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    price_prefix = models.CharField(max_length=5, blank=True, null=True)
    used_lej_coupon_id = models.CharField(max_length=40, blank=True, null=True)
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()
    ground_total = models.DecimalField(max_digits=15, decimal_places=2)
    used_lej_coupon_price = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    other_amount = models.FloatField(default=0)

    class Meta:
        managed = False
        db_table = 'shoppingcart_summaries'


class ShoppingcartPremium(models.Model):
    merchant_order_no = models.CharField(max_length=50)
    service_customer_id = models.CharField(max_length=50)
    price_prefix = models.CharField(max_length=50, default='TWD')
    lej_customer_id = models.CharField(max_length=50, null=True)
    premium_price = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    device_type = models.IntegerField(null=True, default=0)
    date_added = models.DateTimeField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.date_added = timezone.now()
        super(ShoppingcartPremium, self).save(*args, **kwargs)

    class Meta:
        managed = True
        db_table = 'shoppingcart_premium'


class TopexRef(models.Model):
    # pk = models.CharField(primary_key=True, max_length=30)
    customer_id = models.CharField(max_length=30, blank=True, null=True)
    agent_code = models.CharField(max_length=30, blank=True, null=True)
    agent_name = models.CharField(max_length=30, blank=True, null=True)
    agent_email = models.CharField(max_length=30, blank=True, null=True)
    agent_mobile = models.CharField(max_length=30, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'topex_ref'


class Transaction(models.Model):
    id = models.CharField(default=str(uuid.uuid4())[0:30] , primary_key=True, unique=True, max_length=30, db_column='pk')
    transaction_no = models.CharField(max_length=30)
    customer_id = models.CharField(max_length=30)
    guest_id = models.CharField(max_length=255, blank=True, null=True)
    ecredits_price = models.IntegerField(blank=True, null=True)
    price_prefix = models.CharField(max_length=255)
    lejcoupon_id = models.CharField(max_length=30, blank=True, null=True)
    lejcoupon_code = models.CharField(max_length=20, blank=True, null=True)
    total_price = models.DecimalField(max_digits=15, decimal_places=2)
    class_count = models.CharField(max_length=255)
    date_added = models.DateTimeField()
    lej_coupon_price = models.FloatField(blank=True, null=True)
    stripe_charge_id = models.CharField(max_length=255, blank=True, null=True)
    ecpay_merchant_trade_no = models.CharField(max_length=255, blank=True, null=True)
    newebpay_merchant_trade_no = models.CharField(max_length=255, blank=True, null=True)
    device_type = models.IntegerField()
    message_id = models.CharField(max_length=100, blank=True, null=True)
    other_amount = models.FloatField(default=0)
    line_id = models.CharField(max_length=255, blank=True, null=True)
    transaction_type = models.IntegerField(default=0) # 0-regular transaction 1-premium charge 2-fast launch
    # temp = models.FloatField(default=0)

    def save(self, *args, **kwargs):
        self.date_added = timezone.now()
        super(Transaction, self).save(*args, **kwargs)
        
    class Meta:
        managed = False
        db_table = 'transaction'


class TransactionDisputes(models.Model):
    # pk = models.CharField(primary_key=True, max_length=30)
    date_added = models.DateTimeField()
    date_modified = models.DateTimeField()
    booking_no = models.CharField(max_length=20, blank=True, null=True)
    vendor_id = models.CharField(max_length=40, blank=True, null=True)
    customer_name = models.CharField(max_length=64, blank=True, null=True)
    customer_email = models.CharField(max_length=96, blank=True, null=True)
    dispute_type = models.CharField(max_length=255, blank=True, null=True)
    dispute_reason = models.CharField(max_length=255, blank=True, null=True)
    dispute_message = models.TextField(blank=True, null=True)
    dispute_status = models.IntegerField(blank=True, null=True)
    ba_ref_no = models.CharField(max_length=255, blank=True, null=True)
    ba_comment = models.CharField(max_length=255, blank=True, null=True)
    ba_archive_status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'transaction_disputes'


class TransactionItemMerchandises(models.Model):
    # pk = models.CharField(unique=True, max_length=40, blank=True, null=True)
    transaction_item_id = models.CharField(max_length=30, blank=True, null=True)
    merchandise_name = models.CharField(max_length=255, blank=True, null=True)
    merch_option1_name = models.CharField(max_length=255, blank=True, null=True)
    merch_option2_name = models.CharField(max_length=255, blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    each_price = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    total_price = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    price_prefix = models.CharField(max_length=255, blank=True, null=True)
    date_added = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'transaction_item_merchandises'


class TransactionItemProfiles(models.Model):
    id = models.CharField(default=str(uuid.uuid4())[0:30], primary_key=True, unique=True, max_length=30, db_column='pk')
    transaction_item_id = models.CharField(max_length=30)
    profile_id = models.CharField(max_length=30, blank=True, null=True)
    profile_name = models.CharField(max_length=255)
    profile_dob = models.DateField()
    profile_note = models.CharField(max_length=255, blank=True, null=True)
    image_url = models.CharField(max_length=255, blank=True, null=True)
    date_added = models.DateTimeField()
    registration_fee = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)

    def save(self, *args, **kwargs):
        self.date_added = timezone.now()
        super(TransactionItemProfiles, self).save(*args, **kwargs)

    class Meta:
        managed = False
        db_table = 'transaction_item_profiles'


class TransactionItems(models.Model):
    id = models.CharField(default=str(uuid.uuid4())[0:30], primary_key=True, unique=True, max_length=40, db_column='pk')
    transaction_id = models.CharField(max_length=30)
    booking_class_id = models.CharField(max_length=40)
    booking_schedule_id = models.CharField(max_length=40, blank=True, null=True)
    vendor_id = models.CharField(max_length=40)
    vendor_branch_id = models.CharField(max_length=40, blank=True, null=True)
    booking_no = models.CharField(max_length=20, blank=True, null=True)
    class_name = models.CharField(max_length=255)
    option_name = models.CharField(max_length=255)
    schedule_name = models.CharField(max_length=255)
    vendor_name = models.CharField(max_length=255)
    school_coupon_id = models.CharField(max_length=30, blank=True, null=True)
    school_coupon_code = models.CharField(max_length=255, blank=True, null=True)
    original_price = models.DecimalField(max_digits=15, decimal_places=2)
    register_price = models.DecimalField(max_digits=15, decimal_places=2)
    school_coupon_price = models.DecimalField(max_digits=15, decimal_places=2)
    merchandise_price = models.DecimalField(max_digits=15, decimal_places=2)
    total_price = models.DecimalField(max_digits=15, decimal_places=2)
    special_note = models.TextField(blank=True, null=True)
    redeem = models.IntegerField()
    confirm = models.IntegerField()
    booking_status = models.IntegerField(default=1)
    refund_status = models.IntegerField(default=1)
    date_added = models.DateTimeField()
    branch_address = models.CharField(max_length=255, blank=True, null=True)
    branch_name = models.CharField(max_length=255)
    age_min = models.IntegerField(blank=True, null=True)
    age_max = models.IntegerField(blank=True, null=True)
    learner_count = models.IntegerField(blank=True, null=True)
    class_date = models.CharField(max_length=255, blank=True, null=True)
    class_time = models.CharField(max_length=255, blank=True, null=True)
    special_name = models.CharField(max_length=40, blank=True, null=True)
    special_discount = models.DecimalField(default=0.0, max_digits=15, decimal_places=2, blank=True, null=True)
    price_prefix = models.CharField(max_length=5, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.date_added = timezone.now()
        super(TransactionItems, self).save(*args, **kwargs)

    class Meta:
        managed = False
        db_table = 'transaction_items'

class TransactionCounterPay(models.Model):
    guest_id = models.CharField(max_length=255)
    counter_transaction_no = models.CharField(max_length=30, null=True)
    price_prefix = models.CharField(max_length=255)
    total_price = models.DecimalField(max_digits=15, decimal_places=2)
    # To add device_type from platform or not, it's a question
    # device_type = {0:'Guest', 1:'iOS', 2:'Android', 3:'iOS', 4:'Web', 5:'edPOS', 6:'Counter'}
    device_type = models.IntegerField(default=0)
    booking_class_id = models.CharField(max_length=255)
    booking_schedule_id = models.CharField(max_length=255)
    vendor_id = models.CharField(max_length=255)
    vendor_branch_id = models.CharField(max_length=255)
    class_name = models.CharField(max_length=255)
    option_name = models.CharField(max_length=255)
    schedule_name = models.CharField(max_length=255)
    vendor_name = models.CharField(max_length=255)
    branch_name = models.CharField(max_length=255)
    learner_count = models.IntegerField()
    class_date = models.CharField(max_length=255, blank=True, null=True)
    class_time = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    learners = models.CharField(max_length=255)
    date_added = models.DateTimeField()

    def save(self, *args, **kwargs):
        self.date_added = timezone.now()
        super(TransactionCounterPay, self).save(*args, **kwargs)

    class Meta:
        managed = True
        db_table = 'transaction_counterpay'


class Users(models.Model):
    # pk = models.CharField(max_length=40, blank=True, null=True)
    name = models.CharField(max_length=191, blank=True, null=True)
    email = models.CharField(unique=True, max_length=191, blank=True, null=True)
    password = models.CharField(max_length=191, blank=True, null=True)
    remember_token = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'


class VendorActivities(models.Model):
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    method = models.CharField(max_length=255, blank=True, null=True)
    path = models.CharField(max_length=255, blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    controller_name = models.CharField(max_length=255, blank=True, null=True)
    data = models.TextField(blank=True, null=True)
    ip = models.CharField(max_length=255, blank=True, null=True)
    login_info = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vendor_activities'


class VendorBookingCustomers(models.Model):
    # pk = models.CharField(unique=True, max_length=40, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    booking_id = models.CharField(max_length=255, blank=True, null=True)
    customer_id = models.CharField(max_length=255, blank=True, null=True)
    customer_email = models.CharField(max_length=255, blank=True, null=True)
    customer_payment = models.IntegerField(blank=True, null=True)
    customer_open = models.IntegerField(blank=True, null=True)
    customer_hide = models.IntegerField(blank=True, null=True)
    last_nofiy_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vendor_booking_customers'


class VendorBookingSummaries(models.Model):
    # pk = models.CharField(unique=True, max_length=40, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    booking_id = models.CharField(max_length=255, blank=True, null=True)
    customer_id = models.CharField(max_length=255, blank=True, null=True)
    vendor_id = models.CharField(max_length=255, blank=True, null=True)
    grand_total = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    price_prefix = models.CharField(max_length=5, blank=True, null=True)
    input_coupon_code = models.CharField(max_length=255, blank=True, null=True)
    input_coupon_amount = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    input_ecredit_amount = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    special_discount_id = models.CharField(max_length=255, blank=True, null=True)
    special_discount_name = models.CharField(max_length=255, blank=True, null=True)
    special_discount_final_price = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    school_coupon_id = models.CharField(max_length=255, blank=True, null=True)
    school_coupon_final_price = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    sub_total = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vendor_booking_summaries'


class VendorBookings(models.Model):
    # pk = models.CharField(unique=True, max_length=40, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    vendor_id = models.CharField(max_length=255, blank=True, null=True)
    vendor_class_id = models.CharField(max_length=255, blank=True, null=True)
    class_branch_id = models.CharField(max_length=255, blank=True, null=True)
    class_option_id = models.CharField(max_length=255, blank=True, null=True)
    class_schedule_id = models.CharField(max_length=255, blank=True, null=True)
    booking_name = models.CharField(max_length=255, blank=True, null=True)
    booking_message = models.CharField(max_length=255, blank=True, null=True)
    valid_date = models.DateTimeField(blank=True, null=True)
    valid_status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vendor_bookings'


class VendorBranches(models.Model):
    id = models.CharField(primary_key=True, unique=True, max_length=40, db_column='pk')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    vendor_id = models.CharField(max_length=40)
    branch_name = models.CharField(max_length=255, blank=True, null=True)
    branch_email = models.CharField(max_length=255, blank=True, null=True)
    branch_legal_name = models.CharField(max_length=255, blank=True, null=True)
    branch_code = models.CharField(max_length=32, blank=True, null=True)
    contact_name = models.CharField(max_length=32, blank=True, null=True)
    contact_mobile = models.CharField(max_length=32, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    district = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vendor_branches'


class VendorClasses(models.Model):
    id = models.CharField(primary_key=True, unique=True, max_length=40, db_column='pk')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    class_name = models.CharField(max_length=255, blank=True, null=True)
    slug_name = models.CharField(max_length=255, blank=True, null=True)
    vendor = models.ForeignKey('VendorInfos', related_name='vendor_classes', to_field='id', on_delete=models.DO_NOTHING, db_constraint=False, null=True, db_column='vendor_id')
    description = models.TextField(blank=True, null=True)
    age_min = models.IntegerField(blank=True, null=True)
    age_max = models.IntegerField(blank=True, null=True)
    dob_min = models.DateTimeField(blank=True, null=True)
    dob_max = models.DateTimeField(blank=True, null=True)
    cover_image = models.CharField(max_length=255, blank=True, null=True)
    youtube_code = models.CharField(max_length=255, blank=True, null=True)
    class_outline = models.CharField(max_length=255, blank=True, null=True)
    class_tnc = models.CharField(max_length=255, blank=True, null=True)
    teaching_type_1 = models.IntegerField(blank=True, null=True)
    teaching_type_2 = models.IntegerField(blank=True, null=True)
    teaching_type_3 = models.IntegerField(blank=True, null=True)
    teaching_type_4 = models.IntegerField(blank=True, null=True)
    teaching_type_5 = models.IntegerField(blank=True, null=True)
    teaching_type_6 = models.IntegerField(blank=True, null=True)
    teaching_type_7 = models.IntegerField(blank=True, null=True)
    teaching_type_8 = models.IntegerField(blank=True, null=True)
    comment_status = models.IntegerField(blank=True, null=True)
    class_status = models.IntegerField()
    date_status_active = models.DateTimeField(blank=True, null=True)
    date_status_inactive = models.DateTimeField(blank=True, null=True)
    date_status_preview = models.DateTimeField(blank=True, null=True)
    view_count = models.IntegerField(blank=True, null=True)
    ad_paid = models.IntegerField(blank=True, null=True)
    review_count = models.IntegerField()
    review_score = models.IntegerField()
    available_status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vendor_classes'


class VendorImages(models.Model):
    # pk = models.CharField(unique=True, max_length=40, blank=True, null=True)
    class_id = models.CharField(max_length=30, blank=True, null=True)
    image = models.CharField(max_length=255, blank=True, null=True)
    image_list = models.CharField(max_length=255, blank=True, null=True)
    sort_order = models.IntegerField(blank=True, null=True)
    date_added = models.DateTimeField(blank=True, null=True)
    type = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'vendor_images'


class VendorInfos(models.Model):
    id = models.CharField(primary_key=True, unique=True, max_length=40, db_column='pk')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    vendor_name = models.CharField(max_length=64, blank=True, null=True)
    vendor_code = models.CharField(max_length=5, blank=True, null=True)
    vendor_account = models.CharField(max_length=30, blank=True, null=True)
    vendor_raw_password = models.CharField(max_length=80)
    vendor_hashed_password = models.CharField(max_length=80, blank=True, null=True)
    vendor_logo = models.CharField(max_length=255, blank=True, null=True)
    vendor_tagline = models.TextField(blank=True, null=True)
    vendor_description = models.TextField(blank=True, null=True)
    vendor_email = models.TextField(blank=True, null=True)
    vendor_country = models.CharField(max_length=40, blank=True, null=True)
    vendor_currency = models.CharField(max_length=3, blank=True, null=True)
    vendor_city = models.CharField(max_length=40, blank=True, null=True)
    vendor_address = models.TextField(blank=True, null=True)
    vendor_person = models.CharField(max_length=255, blank=True, null=True)
    vendor_contact = models.TextField(blank=True, null=True)
    vendor_person_email = models.CharField(max_length=255, blank=True, null=True)
    vendor_person_contact = models.CharField(max_length=255, blank=True, null=True)
    vendor_website = models.CharField(max_length=255, blank=True, null=True)
    vendor_facebook = models.TextField(blank=True, null=True)
    vendor_instagram = models.TextField(blank=True, null=True)
    vendor_image = models.CharField(max_length=255, blank=True, null=True)
    stripe_account = models.CharField(max_length=40)
    registration_fee = models.DecimalField(max_digits=5, decimal_places=2)
    legal_name = models.CharField(max_length=64, blank=True, null=True)
    vendor_fcm_token = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    sales_status = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vendor_infos'


class VendorMerchandises(models.Model):
    # pk = models.CharField(unique=True, max_length=40, blank=True, null=True)
    vendor_id = models.CharField(max_length=30, blank=True, null=True)
    merch_description = models.CharField(max_length=255, blank=True, null=True)
    merch_image = models.CharField(max_length=255, blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    price_prefix = models.CharField(max_length=255, blank=True, null=True)
    merch_name = models.CharField(max_length=40, blank=True, null=True)
    merch_status = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vendor_merchandises'


class VendorMessages(models.Model):
    # pk = models.CharField(unique=True, max_length=40, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    vendor_id = models.CharField(max_length=255, blank=True, null=True)
    message_title = models.CharField(max_length=255, blank=True, null=True)
    message_body = models.TextField(blank=True, null=True)
    message_image = models.CharField(max_length=255, blank=True, null=True)
    message_url = models.CharField(max_length=255, blank=True, null=True)
    read_status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vendor_messages'


class VendorNotifications(models.Model):
    # pk = models.CharField(primary_key=True, max_length=40)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    vendor_id = models.CharField(max_length=255, blank=True, null=True)
    notification_title = models.CharField(max_length=255, blank=True, null=True)
    notification_body = models.TextField(blank=True, null=True)
    read_status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vendor_notifications'


class VendorPermissions(models.Model):
    # pk = models.CharField(primary_key=True, max_length=30)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    vendor_id = models.CharField(max_length=30, blank=True, null=True)
    max_class_count = models.IntegerField(blank=True, null=True)
    max_timeslot_per_term = models.IntegerField(blank=True, null=True)
    max_coupon_count = models.IntegerField(blank=True, null=True)
    ad_paid_id = models.CharField(max_length=255, blank=True, null=True)
    display_platform = models.CharField(max_length=255, blank=True, null=True)
    payment_gateway = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vendor_permissions'


class VendorTemplates(models.Model):
    # pk = models.CharField(primary_key=True, max_length=40)
    vendor_id = models.CharField(max_length=40, blank=True, null=True)
    page_type = models.CharField(max_length=7)
    template_name = models.CharField(max_length=40, blank=True, null=True)
    template_text = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vendor_templates'


class VendorTypeLogs(models.Model):
    idno = models.AutoField(primary_key=True)
    method = models.CharField(max_length=20, blank=True, null=True)
    vendor_id = models.CharField(max_length=40, blank=True, null=True)
    tb_pk = models.TextField(blank=True, null=True)
    data = models.TextField(blank=True, null=True)
    datetime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'vendor_type_logs'


class VendorTypes(models.Model):
    # pk = models.CharField(unique=True, max_length=40, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    type_name = models.CharField(max_length=255, blank=True, null=True)
    vendor_id = models.CharField(max_length=255, blank=True, null=True)
    lej_discount_id = models.CharField(max_length=40, blank=True, null=True)
    type_discount = models.IntegerField(blank=True, null=True)
    discount_minus = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    discount_percent = models.IntegerField(blank=True, null=True)
    early_bird_day = models.IntegerField(blank=True, null=True)
    companion = models.IntegerField(blank=True, null=True)
    date_start = models.DateField(blank=True, null=True)
    date_end = models.DateField(blank=True, null=True)
    apply_all = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'vendor_types'


class WatchLists(models.Model):
    # pk = models.CharField(unique=True, max_length=30)
    customer_id = models.CharField(max_length=30, blank=True, null=True)
    class_id = models.CharField(max_length=255)
    date_added = models.DateTimeField()
    filters = models.TextField()
    noti_status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'watch_lists'

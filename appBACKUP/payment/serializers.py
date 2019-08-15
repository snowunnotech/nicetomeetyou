from rest_framework import serializers
from payment.models import CurrencyLists, AwardCouponHistories, TransactionItemProfiles

class CurrencyListsSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()
    currency_code = serializers.CharField(max_length=15)
    currency_name = serializers.CharField(max_length=255)
    country_id = serializers.IntegerField()
    exchange_rate = serializers.DecimalField(max_digits=20, decimal_places=6)
    ecredit_rate = serializers.DecimalField(max_digits=20, decimal_places=6)
    allow_payment = serializers.IntegerField()
    stripe_rule = serializers.CharField(max_length=255)
    class Meta:
        model = CurrencyLists
        fields = '__all__'

class AwardCouponHistoriesSerializer(serializers.ModelSerializer):
    customer_id = serializers.CharField(max_length=30)
    award_coupon_id = serializers.CharField(max_length=30)
    award_coupon_code = serializers.CharField(max_length=30)
    award_name = serializers.CharField(max_length=30)
    created_at = serializers.DateTimeField()
    class Meta:
        model = AwardCouponHistories
        fields = '__all__'

class TransactionItemProfilesSerializer(serializers.ModelSerializer):
    transaction_item_id = serializers.CharField(max_length=30)
    profile_id = serializers.CharField(max_length=30)
    profile_name = serializers.CharField(max_length=255)
    profile_dob = serializers.DateField()
    profile_note = serializers.CharField(max_length=255)
    image_url = serializers.CharField(max_length=255)
    date_added = serializers.DateTimeField()
    registration_fee = serializers.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    class Meta:
        model = TransactionItemProfiles
        fields = '__all__'
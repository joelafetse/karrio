from enum import Enum, Flag


class FreightPackagingType(Flag):
    freightcom_pallet = "Pallet"
    freightcom_drum = "Drum"
    freightcom_boxes = "Boxes"
    freightcom_rolls = "Rolls"
    freightcom_pipes_tubes = "Pipes/Tubes"
    freightcom_bales = "Bales"
    freightcom_bags = "Bags"
    freightcom_cylinder = "Cylinder"
    freightcom_pails = "Pails"
    freightcom_reels = "Reels"

    """ Unified Packaging type mapping """
    pallet = freightcom_pallet
    small_box = freightcom_boxes
    medium_box = freightcom_boxes
    large_box = freightcom_boxes


class PaymentType(Flag):  # TODO:: retrieve the complete list of payment types
    check = 'Check'

    sender = "Sender"
    recipient = "Recipient"
    third_party = "Third Party"
    credit_card = "Card"


class Service(Enum):
    freightcom_fedex_priority = "1" 
    freightcom_fedex_first_overnight = "2" 
    freightcom_fedex_ground = "3" 
    freightcom_fedex_standard_overnight = "28"
    freightcom_fedex_2nd_day = "29"
    freightcom_fedex_express_saver = "30"
    freightcom_purolator_air = "4" 
    freightcom_purolator_air_9_am = "5" 
    freightcom_purolator_air_10_30 = "6" 
    freightcom_puroletter = "7" 
    freightcom_puroletter_9_am = "8" 
    freightcom_puroletter_10_30 = "9" 
    freightcom_puro_pak = "10"
    freightcom_puro_pak_9_am = "11"
    freightcom_puro_pak_10_30 = "12"
    freightcom_purolator_ground = "13"
    freightcom_purolator_ground_9_am = "19"
    freightcom_purolator_ground_10_30 = "20"
    freightcom_canada_worldwide_same_day = "14"
    freightcom_canada_worldwide_next_flight_out = "15"
    freightcom_canada_worldwide_air_freight = "16"
    freightcom_canada_worldwide_ltl = "17"
    freightcom_dhl_international_express = "106" 
    freightcom_ups_express_next_day_air = "600" 
    freightcom_ups_expedited_second_day_air = "601" 
    freightcom_ups_worldwide_express = "602" 
    freightcom_ups_worldwide_expedited = "603" 
    freightcom_ups_standard_ground = "604" 
    freightcom_ups_express_early_am_next_day_air_early_am = "605" 
    freightcom_ups_three_day_select = "606" 
    freightcom_ups_saver = "607" 
    freightcom_ups_ground = "608" 
    freightcom_next_day_saver = "609" 
    freightcom_worldwide_express_plus = "610" 
    freightcom_second_day_air_am = "611" 
    freightcom_canada_post_priority = "500" 
    freightcom_canada_post_xpress_post = "501" 
    freightcom_canada_post_expedited = "502" 
    freightcom_canada_post_regular = "503" 
    freightcom_canada_post_xpress_post_usa = "504" 
    freightcom_canada_post_xpress_post_intl = "505" 
    freightcom_canada_post_air_parcel_intl = "506" 
    freightcom_canada_post_surface_parcel_intl = "507" 
    freightcom_canada_post_expedited_parcel_usa = "508" 
    freightcom_tst_ltl = "1100"
    freightcom_ltl_chicago_suburban_express = "1500"
    freightcom_ltl_fedex_freight_east = "1501"
    freightcom_ltl_fedex_freight_west = "1502"
    freightcom_ltl_mid_states_express = "1503"
    freightcom_ltl_new_england_motor_freight = "1504"
    freightcom_ltl_new_penn = "1505"
    freightcom_ltl_oak_harbor = "1506"
    freightcom_ltl_pitt_ohio = "1507"
    freightcom_ltl_r_l_carriers = "1508"
    freightcom_ltl_saia = "1509"
    freightcom_ltl_usf_reddaway = "1510"
    freightcom_ltl_vitran_express = "1511"
    freightcom_ltl_wilson_trucking = "1512"
    freightcom_ltl_yellow_transportation = "1513"
    freightcom_ltl_roadway = "1514"
    freightcom_ltl_fedex_national = "1515"
    freightcom_wilson_trucking_tfc = "1800"
    freightcom_aaa_cooper_transportation = "1801"
    freightcom_roadrunner_dawes = "1802"
    freightcom_new_england_motor_freight = "1803"
    freightcom_new_penn_motor_express = "1804"
    freightcom_dayton_freight = "1805"
    freightcom_southeastern_freightway = "1806"
    freightcom_saia_inc = "1807"
    freightcom_conway = "1808"
    freightcom_roadway = "1809"
    freightcom_usf_reddaway = "1810"
    freightcom_usf_holland = "1811"
    freightcom_dependable_highway_express = "1812"
    freightcom_day_and_ross = "1813"
    freightcom_day_and_ross_r_and_l = "1814"
    freightcom_ups = "1815"
    freightcom_aaa_cooper = "1816"
    freightcom_ama_transportation = "1817"
    freightcom_averitt_express = "1818"
    freightcom_central_freight = "1819"
    freightcom_conway_us = "1820"
    freightcom_dayton = "1821"
    freightcom_drug_transport = "1822"
    freightcom_estes = "1823"
    freightcom_land_air_express = "1824"
    freightcom_fedex_west = "1825"
    freightcom_fedex_national = "1826"
    freightcom_usf_holland_us = "1827"
    freightcom_lakeville_m_express = "1828"
    freightcom_milan_express = "1829"
    freightcom_nebraska_transport = "1830"
    freightcom_new_england = "1831"
    freightcom_new_penn = "1832"
    freightcom_a_duie_pyle = "1833"
    freightcom_roadway_us = "1834"
    freightcom_usf_reddaway_us = "1835"
    freightcom_rhody_transportation = "1836"
    freightcom_saia_motor_freight = "1837"
    freightcom_southeastern_frgt = "1838"
    freightcom_pitt_ohio = "1839"
    freightcom_ward = "1840"
    freightcom_wilson = "1841"
    freightcom_chi_cargo = "1842"
    freightcom_tax_air = "1843"
    freightcom_fedex_east = "1844"
    freightcom_central_transport = "1845"
    freightcom_roadrunner = "1846"
    freightcom_r_and_l_carriers = "1847"
    freightcom_estes_us = "1848"
    freightcom_yrc_roadway = "1849"
    freightcom_central_transport_us = "1850"
    freightcom_absolute_transportation_services = "1851"
    freightcom_blue_sky_express = "1852"
    freightcom_galasso_trucking = "1853"
    freightcom_griley_air_freight = "1854"
    freightcom_jet_transportation = "1855"
    freightcom_metro_transportation_logistics = "1856"
    freightcom_oak_harbor = "1857"
    freightcom_stream_links_express = "1858"
    freightcom_tiffany_trucking = "1859"
    freightcom_ups_freight = "1860"
    freightcom_roadrunner_us = "1861"
    freightcom_global_mail_parcel_priority = "3500"
    freightcom_global_mail_parcel_standard = "3501"
    freightcom_global_mail_packet_plus_priority = "3502"
    freightcom_global_mail_packet_priority = "3503"
    freightcom_global_mail_packet_standard = "3504"
    freightcom_global_mail_business_priority = "3505"
    freightcom_global_mail_business_standard = "3506"
    freightcom_global_mail_parcel_direct_priority = "3507"
    freightcom_global_mail_parcel_direct_standard = "3508"


class Option(Flag):
    freightcom_saturday_pickup_required = "saturdayPickupRequired"
    freightcom_homeland_security = "homelandSecurity"
    freightcom_exhibition_convention_site = "exhibitionConventionSite"
    freightcom_military_base_delivery = "militaryBaseDelivery"
    freightcom_customs_in_bond_freight = "customsIn_bondFreight"
    freightcom_limited_access = "limitedAccess"
    freightcom_excess_length = "excessLength"
    freightcom_tailgate_pickup = "tailgatePickup"
    freightcom_residential_pickup = "residentialPickup"
    freightcom_cross_border_fee = "crossBorderFee"
    freightcom_notify_recipient = "notifyRecipient"
    freightcom_single_shipment = "singleShipment"
    freightcom_tailgate_delivery = "tailgateDelivery"
    freightcom_residential_delivery = "residentialDelivery"
    freightcom_insurance_type = "insuranceType"
    freightcom_inside_delivery = "insideDelivery"
    freightcom_is_saturday_service = "isSaturdayService"
    freightcom_dangerous_goods_type = "dangerousGoodsType"
    freightcom_stackable = "stackable"


class FreightClass(Enum):
    freightcom_freight_class_50 = 50
    freightcom_freight_class_55 = 55
    freightcom_freight_class_60 = 60
    freightcom_freight_class_65 = 65
    freightcom_freight_class_70 = 70
    freightcom_freight_class_77 = 77
    freightcom_freight_class_77_5 = 77.5
    freightcom_freight_class_85 = 85
    freightcom_freight_class_92_5 = 92.5
    freightcom_freight_class_100 = 100
    freightcom_freight_class_110 = 110
    freightcom_freight_class_125 = 125
    freightcom_freight_class_150 = 150
    freightcom_freight_class_175 = 175
    freightcom_freight_class_200 = 200
    freightcom_freight_class_250 = 250
    freightcom_freight_class_300 = 300
    freightcom_freight_class_400 = 400

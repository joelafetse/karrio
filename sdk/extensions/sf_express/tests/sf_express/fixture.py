import karrio

gateway = karrio.gateway["sf_express"].create(
    dict(
        partner_id="partner_id",
        check_word="check_word",
    )
)

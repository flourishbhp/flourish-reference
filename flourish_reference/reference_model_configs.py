from edc_reference import site_reference_configs

site_reference_configs.register_from_visit_schedule(
    visit_models={
        'edc_appointment.appointment': ['flourish_caregiver.maternalvisit'],
        'flourish_child.appointment': ['flourish_child.childvisit'],
        'pre_flourish.appointment': ['pre_flourish.preflourishvisit'],
        'flourish_facet.appointment': ['flourish_facet.facetvisit']
    })

configs = {
    'flourish_caregiver.caregivergadanxietyscreening': ['anxiety_score'],
    'flourish_caregiver.caregiverphqdeprscreening': ['depression_score',
                                                     'self_harm'],
    'flourish_caregiver.caregiveredinburghdeprscreening': ['depression_score',
                                                           'self_harm'],
    'flourish_caregiver.caregiverphqreferral': ['referred_to'],
    'flourish_caregiver.caregiveredinburghreferral': ['referred_to'],
    'flourish_caregiver.caregivergadreferral': ['referred_to'],
    'flourish_caregiver.maternalvisit': ['info_source'],
    'flourish_child.childvisit': ['info_source'],
    'flourish_child.childphqreferral': ['referred_to'],
    'flourish_child.childgadreferral': ['referred_to'],
    'flourish_caregiver.hivdisclosurestatusa': ['disclosed_status'],
    'flourish_caregiver.hivdisclosurestatusb': ['disclosed_status'],
    'flourish_caregiver.hivdisclosurestatusc': ['disclosed_status'],
    'flourish_child.childsociodemographic': ['attend_school', 'working'],
    'flourish_child.childphqdepressionscreening': ['depression_score',
                                                   'self_harm',
                                                   'self_harm_thoughts',
                                                   'suidice_attempt'],
    'flourish_child.childgadanxietyscreening': ['anxiety_score'],
    'flourish_caregiver.hivrapidtestcounseling': ['result_date'],
    'flourish_child.birthdata': ['congenital_anomalities'],
    'flourish_caregiver.tbstudyeligibility': ['tb_participation'],
    'flourish_caregiver.hitsscreening': ['score'],
    'flourish_caregiver.hitsreferral': ['referred_to'],
    'flourish_caregiver.relationshipfatherinvolvement': ['partner_present',],
    'flourish_caregiver.tbengagement': ['interview_consent'],
    'flourish_caregiver.breastmilk6months': ['milk_collected'],
    'flourish_caregiver.breastmilkbirth': ['milk_collected'],
    'flourish_caregiver.tbinterview': ['interview_language'],
    'flourish_child.tbadolengagement': ['interview_consent'],
    'flourish_child.tbadolinterview': ['interview_language'],
    'flourish_child.tblabresultsadol': ['quantiferon_result'],
    'flourish_child.tbvisitscreeningadolescent': ['cough_duration', 'fever_duration',
                                                  'night_sweats', 'weight_loss'],
    'flourish_child.tbpresencehouseholdmembersadol': ['tb_referral', ],
    'flourish_child.hivtestingadol': ['seen_by_healthcare', 'referred_for_treatment'],

    # FACET

    'flourish_facet.anxietyscreeninggad7': ['anxiety_score'],
    'flourish_facet.depressionscreeningphq9': ['depression_score', 'self_harm'],
    'flourish_facet.depressionscreeningedinburgh': ['depression_score', 'self_harm'],
    'flourish_facet.facetcaregiverphqreferral': ['referred_to'],
    'flourish_facet.facetcaregiveredinburghreferral': ['referred_to'],
    'flourish_facet.facetcaregivergadreferral': ['referred_to'],
    'flourish_facet.intimatepartnerviolence': ['referral'],
    'flourish_facet.childhivtesting': ['preferred_test_venue'],


}

for reference_name, fields in configs.items():
    site_reference_configs.add_fields_to_config(
        name=reference_name, fields=fields)

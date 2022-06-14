from edc_reference import site_reference_configs

site_reference_configs.register_from_visit_schedule(
    visit_models={
        'edc_appointment.appointment': ['flourish_caregiver.maternalvisit'],
        'flourish_child.appointment': ['flourish_child.childvisit'],
        })

configs = {
    'flourish_caregiver.caregivergadanxietyscreening': ['anxiety_score'],
    'flourish_caregiver.caregiverphqdeprscreening': ['depression_score',
                                                     'self_harm'],
    'flourish_caregiver.caregiveredinburghdeprscreening': ['depression_score',
                                                           'self_harm'],
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
    'flourish_caregiver.breastfeedingquestionnaire': ['feeding_hiv_status'],
    'flourish_caregiver.tbstudyeligibility': ['tb_participation'],
}

for reference_name, fields in configs.items():
    site_reference_configs.add_fields_to_config(
        name=reference_name, fields=fields)

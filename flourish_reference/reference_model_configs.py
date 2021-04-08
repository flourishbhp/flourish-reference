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
                                                           'self_harm']
    }

for reference_name, fields in configs.items():
    site_reference_configs.add_fields_to_config(
        name=reference_name, fields=fields)

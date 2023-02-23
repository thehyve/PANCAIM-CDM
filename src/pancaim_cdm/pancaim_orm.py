from dataclasses import dataclass
from types import SimpleNamespace

from sqlalchemy import Column, Integer, Text, Numeric, Date, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

CDM_SCHEMA = 'cdm_schema'


# These table classes are used to have only one place where the table
# and field names are captured. If a name of a table or field needs to
# change, it can be done so by updating the field string and not the
# variable name. That way the ETL repos using this CDM will not have to
# be updated in case of a name change.
@dataclass
class Table:
    name: str
    fields: SimpleNamespace


_person = Table(
    name='person',
    fields=SimpleNamespace(
        pancaim_id='pancaim_id',
        pancaim_id_raw_value='pancaim_id_raw_value',

        age_at_diagnosis='age_at_diagnosis',
        date_of_birth='date_of_birth',                                  # Probable
        date_of_death='date_of_death',
        date_of_diagnosis='date_of_diagnosis',                          # Probable
        date_of_first_contact='date_of_first_contact',                  # Probable
        date_of_interview='date_of_interview',                          # Probable
        date_of_last_contact='date_of_last_contact',                    # Probable
        ecog_scale='ecog_scale',
        ethnicity='ethnicity',
        other_associated_illnesses='other_associated_illnesses',
        resectional_surgery='resectional_surgery',
        sex='sex',
        surgery='surgery',
        vital_status='vital_status',

        age_at_diagnosis_raw_value='age_at_diagnosis_raw_value',
        date_of_birth_raw_value='date_of_birth_raw_value',                              # Probable
        date_of_death_raw_value='date_of_death_raw_value',
        date_of_diagnosis_raw_value='date_of_diagnosis_raw_value',                      # Probable
        date_of_first_contact_raw_value='date_of_first_contact_raw_value',              # Probable
        date_of_interview_raw_value='date_of_interview_raw_value',                      # Probable
        date_of_last_contact_raw_value='date_of_last_contact_raw_value',                # Probable
        ecog_scale_raw_value='ecog_scale_raw_value',
        ethnicity_raw_value='ethnicity_raw_value',
        other_associated_illnesses_raw_value='other_associated_illnesses_raw_value',
        resectional_surgery_raw_value='resectional_surgery_raw_value',
        sex_raw_value='sex_raw_value',
        surgery_raw_value='surgery_raw_value',
        vital_status_raw_value='vital_status_raw_value',
    )
)

_body_measurement = Table(
    name='body_measurement',
    fields=SimpleNamespace(
        body_measurement_id='body_measurement_id',
        pancaim_id='pancaim_id',

        body_measurement_date='body_measurement_date',
        body_measurement_date_raw_value='body_measurement_date_raw_value',

        height='height',
        weight='weight',

        height_raw_value='height_raw_value',
        weight_raw_value='weight_raw_value',
    )
)

_lab = Table(
    name='lab',
    fields=SimpleNamespace(
        lab_id='lab_id',
        pancaim_id='pancaim_id',

        lab_date='lab_date',
        lab_date_raw_value='lab_date_raw_value',

        albumin='albumin',
        alt='alt',
        ast='ast',
        bilirubin_total='bilirubin_total',
        cholesterol='cholesterol',
        crp='crp',
        fibrinogen='fibrinogen',                                # Probable
        fosfatase='fosfatase',
        glucose='glucose',
        gt_ggtp='gt_ggtp',
        hb='hb',
        hematocrit='hematocrit',
        leukocytes='leukocytes',
        plateletes='plateletes',
        protrombin='protrombin',
        triglycerides='triglycerides',                          # Probable
        tromboplastin='tromboplastin',                          # Probable

        albumin_raw_value='albumin_raw_value',
        alt_raw_value='alt_raw_value',
        ast_raw_value='ast_raw_value',
        bilirubin_total_raw_value='bilirubin_total_raw_value',
        cholesterol_raw_value='cholesterol_raw_value',
        crp_raw_value='crp_raw_value',
        fibrinogen_raw_value='fibrinogen_raw_value',            # Probable
        fosfatase_raw_value='fosfatase_raw_value',
        glucose_raw_value='glucose_raw_value',
        gt_ggtp_raw_value='gt_ggtp_raw_value',
        hb_raw_value='hb_raw_value',
        hematocrit_raw_value='hematocrit_raw_value',
        leukocytes_raw_value='leukocytes_raw_value',
        plateletes_raw_value='plateletes_raw_value',
        protrombin_raw_value='protrombin_raw_value',
        triglycerides_raw_value='triglycerides_raw_value',      # Probable
        tromboplastin_raw_value='tromboplastin_raw_value',      # Probable
    )
)

_lab2 = Table(
    name='lab2',
    fields=SimpleNamespace(
        lab2_id='lab2_id',
        pancaim_id='pancaim_id',

        lab2_date='lab2_date',
        lab2_date_raw_value='lab2_date_raw_value',

        ca_19_9='ca_19_9',
        cea='cea',

        ca_19_9_raw_value='ca_19_9_raw_value',
        cea_raw_value='cea_raw_value',
    )
)

_prognosis = Table(
    name='prognosis',
    fields=SimpleNamespace(
        prognosis_id='prognosis_id',
        pancaim_id='pancaim_id',

        prognosis_date='prognosis_date',
        prognosis_date_raw_value='prognosis_date_raw_value',

        time_at_risk_to_death_variable='time_at_risk_to_death_variable',
        time_at_risk_variable_in_months='time_at_risk_variable_in_months',

        time_at_risk_to_death_variable_raw_value='time_at_risk_to_death_variable_raw_value',
        time_at_risk_variable_in_months_raw_value='time_at_risk_variable_in_months_raw_value',
    )
)

_surgery = Table(
    name='surgery',
    fields=SimpleNamespace(
        surgery_id='surgery_id',
        pancaim_id='pancaim_id',

        date_of_surgery='date_of_surgery',                                          # Probable
        surgery_purpose='surgery_purpose',
        surgical_technique='surgical_technique',
        year_of_surgery='year_of_surgery',

        date_of_surgery_raw_value='date_of_surgery_raw_value',                      # Probable
        surgery_purpose_raw_value='surgery_purpose_raw_value',
        surgical_technique_raw_value='surgical_technique_raw_value',
        year_of_surgery_raw_value='year_of_surgery_raw_value',
    )
)

_therapy = Table(
    name='therapy',
    fields=SimpleNamespace(
        therapy_id='therapy_id',

        pancaim_id='pancaim_id',

        adjuvant_chemotherapy='adjuvant_chemotherapy',
        adjuvant_radiotherapy='adjuvant_radiotherapy',
        date_start_adjuvant_chemotherapy='date_start_adjuvant_chemotherapy',
        neoadjuvant_chemotherapy='neoadjuvant_chemotherapy',
        neoadjuvant_radiotherapy='neoadjuvant_radiotherapy',
        purpose_of_neoadjuvant_chemotherapy='purpose_of_neoadjuvant_chemotherapy',
        purpose_of_neoadjuvant_radiotherapy='purpose_of_neoadjuvant_radiotherapy',

        adjuvant_chemotherapy_raw_value='adjuvant_chemotherapy_raw_value',
        adjuvant_radiotherapy_raw_value='adjuvant_radiotherapy_raw_value',
        date_start_adjuvant_chemotherapy_raw_value='date_start_adjuvant_chemotherapy_raw_value',
        neoadjuvant_chemotherapy_raw_value='neoadjuvant_chemotherapy_raw_value',
        neoadjuvant_radiotherapy_raw_value='neoadjuvant_radiotherapy_raw_value',
        purpose_of_neoadjuvant_chemotherapy_raw_value='purpose_of_neoadjuvant_chemotherapy_raw_value',
        purpose_of_neoadjuvant_radiotherapy_raw_value='purpose_of_neoadjuvant_radiotherapy_raw_value',
    )
)

_tumor = Table(
    name='tumor',
    fields=SimpleNamespace(
        tumor_id='tumor_id',

        pancaim_id='pancaim_id',

        tumor_date='tumor_date',
        tumor_date_raw_value='tumor_date_raw_value',

        clinical_tnm='clinical_tnm',
        combined_tnm='combined_tnm',                                    # Probable
        histology_description='histology_description',
        histology_present='histology_present',
        invasion_of_other_organs='invasion_of_other_organs',
        pathological_tnm='pathological_tnm',
        pm='pm',
        pn='pn',
        pt='pt',
        reconstructed_tnm='reconstructed_tnm',                          # Probable
        resectability_tnm='resectability_tnm',                          # Probable
        tumor_location='tumor_location',
        tumor_size='tumor_size',

        clinical_tnm_raw_value='clinical_tnm_raw_value',
        combined_tnm_raw_value='combined_tnm_raw_value',                            # Probable
        histology_description_raw_value='histology_description_raw_value',
        histology_present_raw_value='histology_present_raw_value',
        invasion_of_other_organs_raw_value='invasion_of_other_organs_raw_value',
        pathological_tnm_raw_value='pathological_tnm_raw_value',
        pm_raw_value='pm_raw_value',
        pn_raw_value='pn_raw_value',
        pt_raw_value='pt_raw_value',
        reconstructed_tnm_raw_value='reconstructed_tnm_raw_value',                  # Probable
        resectability_tnm_raw_value='resectability_tnm_raw_value',                  # Probable
        tumor_location_raw_value='tumor_location_raw_value',
        tumor_size_raw_value='tumor_size_raw_value',
    )
)


class Person(Base):
    __tablename__ = _person.name
    __table_args__ = {'schema': CDM_SCHEMA}

    pancaim_id = Column(Integer, primary_key=True, name=_person.fields.pancaim_id)
    pancaim_id_raw_value = Column(Text, name=_person.fields.pancaim_id_raw_value)

    age_at_diagnosis = Column(Numeric, name=_person.fields.age_at_diagnosis)                            # Var type is currently undecided in model (numeric vs integer)
    date_of_birth = Column(Date, name=_person.fields.date_of_birth)
    date_of_death = Column(Date, name=_person.fields.date_of_death)
    date_of_diagnosis = Column(Date, name=_person.fields.date_of_diagnosis)
    date_of_first_contact = Column(Date, name=_person.fields.date_of_first_contact)
    date_of_interview = Column(Date, name=_person.fields.date_of_interview)
    date_of_last_contact = Column(Date, name=_person.fields.date_of_last_contact)
    ecog_scale = Column(Integer, name=_person.fields.ecog_scale)
    ethnicity = Column(Text, name=_person.fields.ethnicity)
    other_associated_illnesses = Column(Text, name=_person.fields.other_associated_illnesses)           # Var type currently undecided, probably Text
    resectional_surgery = Column(Boolean, name=_person.fields.resectional_surgery)
    sex = Column(Text, nullable=False, name=_person.fields.sex)
    surgery = Column(Boolean, name=_person.fields.surgery)
    vital_status = Column(Text, name=_person.fields.vital_status)

    age_at_diagnosis_raw_value = Column(Text, name=_person.fields.age_at_diagnosis_raw_value)
    date_of_birth_raw_value = Column(Text, name=_person.fields.date_of_birth_raw_value)
    date_of_death_raw_value = Column(Text, name=_person.fields.date_of_death_raw_value)
    date_of_diagnosis_raw_value = Column(Text, name=_person.fields.date_of_diagnosis_raw_value)
    date_of_first_contact_raw_value = Column(Text, name=_person.fields.date_of_first_contact_raw_value)
    date_of_interview_raw_value = Column(Text, name=_person.fields.date_of_interview_raw_value)
    date_of_last_contact_raw_value = Column(Text, name=_person.fields.date_of_last_contact_raw_value)
    ecog_scale_raw_value = Column(Text, name=_person.fields.ecog_scale_raw_value)
    ethnicity_raw_value = Column(Text, name=_person.fields.ethnicity_raw_value)
    other_associated_illnesses_raw_value = Column(Text, name=_person.fields.other_associated_illnesses_raw_value)
    resectional_surgery_raw_value = Column(Text, name=_person.fields.resectional_surgery_raw_value)
    sex_raw_value = Column(Text, name=_person.fields.sex_raw_value)
    surgery_raw_value = Column(Text, name=_person.fields.surgery_raw_value)
    vital_status_raw_value = Column(Text, name=_person.fields.vital_status_raw_value)


class BodyMeasurement(Base):
    __tablename__ = _body_measurement.name
    __table_args__ = {'schema': CDM_SCHEMA}

    body_measurement_id = Column(Integer, primary_key=True, name=_body_measurement.fields.body_measurement_id)

    pancaim_id = Column(ForeignKey(f'{CDM_SCHEMA}.{_person.name}.{_person.fields.pancaim_id}', ondelete="CASCADE"),
                        nullable=False, name=_body_measurement.fields.pancaim_id)

    body_measurement_date = Column(Date, name=_body_measurement.fields.body_measurement_date, nullable=False)
    body_measurement_date_raw_value = Column(Date, name=_body_measurement.fields.body_measurement_date_raw_value, nullable=False)

    height = Column(Integer, name=_body_measurement.fields.height)
    weight = Column(Numeric, name=_body_measurement.fields.weight)

    height_raw_value = Column(Text, name=_body_measurement.fields.height_raw_value)
    weight_raw_value = Column(Text, name=_body_measurement.fields.weight_raw_value)


class Lab(Base):
    __tablename__ = _lab.name
    __table_args__ = {'schema': CDM_SCHEMA}

    lab_id = Column(Integer, primary_key=True, name=_lab.fields.lab_id)

    pancaim_id = Column(ForeignKey(f'{CDM_SCHEMA}.{_person.name}.{_person.fields.pancaim_id}', ondelete="CASCADE"),
                        nullable=False, name=_lab.fields.pancaim_id)

    lab_date = Column(Date, name=_lab.fields.lab_date, nullable=False)
    lab_date_raw_value = Column(Date, name=_lab.fields.lab_date_raw_value, nullable=False)

    albumin = Column(Numeric, name=_lab.fields.albumin)
    alt = Column(Numeric, name=_lab.fields.alt)
    ast = Column(Numeric, name=_lab.fields.ast)
    bilirubin_total = Column(Numeric, name=_lab.fields.bilirubin_total)
    cholesterol = Column(Numeric, name=_lab.fields.cholesterol)
    crp = Column(Numeric, name=_lab.fields.crp)
    fibrinogen = Column(Numeric, name=_lab.fields.fibrinogen)                   # Probable
    fosfatase = Column(Numeric, name=_lab.fields.fosfatase)
    glucose = Column(Numeric, name=_lab.fields.glucose)
    gt_ggtp = Column(Numeric, name=_lab.fields.gt_ggtp)
    hb = Column(Numeric, name=_lab.fields.hb)
    hematocrit = Column(Numeric, name=_lab.fields.hematocrit)
    leukocytes = Column(Numeric, name=_lab.fields.leukocytes)
    plateletes = Column(Numeric, name=_lab.fields.plateletes)
    protrombin = Column(Numeric, name=_lab.fields.protrombin)
    triglycerides = Column(Numeric, name=_lab.fields.triglycerides)             # Probable
    tromboplastin = Column(Numeric, name=_lab.fields.tromboplastin)             # Probable

    albumin_raw_value = Column(Text, name=_lab.fields.albumin_raw_value)
    alt_raw_value = Column(Text, name=_lab.fields.alt_raw_value)
    ast_raw_value = Column(Text, name=_lab.fields.ast_raw_value)
    bilirubin_total_raw_value = Column(Text, name=_lab.fields.bilirubin_total_raw_value)
    cholesterol_raw_value = Column(Text, name=_lab.fields.cholesterol_raw_value)
    crp_raw_value = Column(Text, name=_lab.fields.crp_raw_value)
    fibrinogen_raw_value = Column(Text, name=_lab.fields.fibrinogen_raw_value)                   # Probable
    fosfatase_raw_value = Column(Text, name=_lab.fields.fosfatase_raw_value)
    glucose_raw_value = Column(Text, name=_lab.fields.glucose_raw_value)
    gt_ggtp_raw_value = Column(Text, name=_lab.fields.gt_ggtp_raw_value)
    hb_raw_value = Column(Text, name=_lab.fields.hb_raw_value)
    hematocrit_raw_value = Column(Text, name=_lab.fields.hematocrit_raw_value)
    leukocytes_raw_value = Column(Text, name=_lab.fields.leukocytes_raw_value)
    plateletes_raw_value = Column(Text, name=_lab.fields.plateletes_raw_value)
    protrombin_raw_value = Column(Text, name=_lab.fields.protrombin_raw_value)
    triglycerides_raw_value = Column(Text, name=_lab.fields.triglycerides_raw_value)             # Probable
    tromboplastin_raw_value = Column(Text, name=_lab.fields.tromboplastin_raw_value)             # Probable


class Lab2(Base):
    __tablename__ = _lab2.name
    __table_args__ = {'schema': CDM_SCHEMA}

    lab2_id = Column(Integer, primary_key=True, name=_lab2.fields.lab2_id)

    pancaim_id = Column(ForeignKey(f'{CDM_SCHEMA}.{_person.name}.{_person.fields.pancaim_id}', ondelete="CASCADE"),
                        nullable=False, name=_lab2.fields.pancaim_id)

    lab2_date = Column(Date, name=_lab2.fields.lab2_date, nullable=False)
    lab2_date_raw_value = Column(Date, name=_lab2.fields.lab2_date_raw_value, nullable=False)

    ca_19_9 = Column(Numeric, name=_lab2.fields.ca_19_9)
    cea = Column(Numeric, name=_lab2.fields.cea)

    ca_19_9_raw_value = Column(Text, name=_lab2.fields.ca_19_9_raw_value)
    cea_raw_value = Column(Text, name=_lab2.fields.cea_raw_value)


class Prognosis(Base):
    __tablename__ = _prognosis.name
    __table_args__ = {'schema': CDM_SCHEMA}

    prognosis_id = Column(Integer, primary_key=True, name=_prognosis.fields.prognosis_id)

    pancaim_id = Column(ForeignKey(f'{CDM_SCHEMA}.{_person.name}.{_person.fields.pancaim_id}', ondelete="CASCADE"),
                        nullable=False, name=_prognosis.fields.pancaim_id)

    prognosis_date = Column(Date, name=_prognosis.fields.prognosis_date, nullable=False)
    prognosis_date_raw_value = Column(Date, name=_prognosis.fields.prognosis_date_raw_value, nullable=False)

    time_at_risk_to_death_variable = Column(Numeric, name=_prognosis.fields.time_at_risk_to_death_variable)
    time_at_risk_variable_in_months = Column(Numeric, name=_prognosis.fields.time_at_risk_variable_in_months)

    time_at_risk_to_death_variable_raw_value = Column(Text, name=_prognosis.fields.time_at_risk_to_death_variable_raw_value)
    time_at_risk_variable_in_months_raw_value = Column(Text, name=_prognosis.fields.time_at_risk_variable_in_months_raw_value)


class Surgery(Base):
    __tablename__ = _surgery.name
    __table_args__ = {'schema': CDM_SCHEMA}

    surgery_id = Column(Integer, primary_key=True, name=_surgery.fields.surgery_id)

    pancaim_id = Column(ForeignKey(f'{CDM_SCHEMA}.{_person.name}.{_person.fields.pancaim_id}', ondelete="CASCADE"),
                        nullable=False, name=_surgery.fields.pancaim_id)

    date_of_surgery = Column(Date, name=_surgery.fields.date_of_surgery, nullable=False)                                # Probable
    surgery_purpose = Column(Text, name=_surgery.fields.surgery_purpose)
    surgical_technique = Column(Text, name=_surgery.fields.surgical_technique)
    year_of_surgery = Column(Integer, name=_surgery.fields.year_of_surgery)                             # Model specifies Date type, but "year" as Integer makes more sense.

    date_of_surgery_raw_value = Column(Text, name=_surgery.fields.date_of_surgery_raw_value, nullable=False)            # Probable
    surgery_purpose_raw_value = Column(Text, name=_surgery.fields.surgery_purpose_raw_value)
    surgical_technique_raw_value = Column(Text, name=_surgery.fields.surgical_technique_raw_value)
    year_of_surgery_raw_value = Column(Text, name=_surgery.fields.year_of_surgery_raw_value)


class Therapy(Base):
    __tablename__ = _therapy.name
    __table_args__ = {'schema': CDM_SCHEMA}

    therapy_id = Column(Integer, primary_key=True, name=_therapy.fields.therapy_id)

    pancaim_id = Column(ForeignKey(f'{CDM_SCHEMA}.{_person.name}.{_person.fields.pancaim_id}', ondelete="CASCADE"),
                        nullable=False, name=_therapy.fields.pancaim_id)

    adjuvant_chemotherapy = Column(Text, name=_therapy.fields.adjuvant_chemotherapy)
    adjuvant_radiotherapy = Column(Text, name=_therapy.fields.adjuvant_radiotherapy)
    date_start_adjuvant_chemotherapy = Column(Date, name=_therapy.fields.date_start_adjuvant_chemotherapy)
    neoadjuvant_chemotherapy = Column(Text, name=_therapy.fields.neoadjuvant_chemotherapy)
    neoadjuvant_radiotherapy = Column(Text, name=_therapy.fields.neoadjuvant_radiotherapy)
    purpose_of_neoadjuvant_chemotherapy = Column(Text, name=_therapy.fields.purpose_of_neoadjuvant_chemotherapy)
    purpose_of_neoadjuvant_radiotherapy = Column(Text, name=_therapy.fields.purpose_of_neoadjuvant_radiotherapy)

    adjuvant_chemotherapy_raw_value = Column(Text, name=_therapy.fields.adjuvant_chemotherapy_raw_value)
    adjuvant_radiotherapy_raw_value = Column(Text, name=_therapy.fields.adjuvant_radiotherapy_raw_value)
    date_start_adjuvant_chemotherapy_raw_value = Column(Text, name=_therapy.fields.date_start_adjuvant_chemotherapy_raw_value)
    neoadjuvant_chemotherapy_raw_value = Column(Text, name=_therapy.fields.neoadjuvant_chemotherapy_raw_value)
    neoadjuvant_radiotherapy_raw_value = Column(Text, name=_therapy.fields.neoadjuvant_radiotherapy_raw_value)
    purpose_of_neoadjuvant_chemotherapy_raw_value = Column(Text, name=_therapy.fields.purpose_of_neoadjuvant_chemotherapy_raw_value)
    purpose_of_neoadjuvant_radiotherapy_raw_value = Column(Text, name=_therapy.fields.purpose_of_neoadjuvant_radiotherapy_raw_value)


class Tumor(Base):
    __tablename__ = _tumor.name
    __table_args__ = {'schema': CDM_SCHEMA}

    tumor_id = Column(Integer, primary_key=True, name=_tumor.fields.tumor_id)

    pancaim_id = Column(ForeignKey(f'{CDM_SCHEMA}.{_person.name}.{_person.fields.pancaim_id}', ondelete="CASCADE"),
                        nullable=False, name=_tumor.fields.pancaim_id)

    tumor_date = Column(Date, name=_tumor.fields.tumor_date, nullable=False)
    tumor_date_raw_value = Column(Date, name=_tumor.fields.tumor_date_raw_value, nullable=False)

    clinical_tnm = Column(Text, name=_tumor.fields.clinical_tnm)
    combined_tnm = Column(Text, name=_tumor.fields.combined_tnm)                                # Probable
    histology_description = Column(Text, name=_tumor.fields.histology_description)
    histology_present = Column(Text, name=_tumor.fields.histology_present)
    invasion_of_other_organs = Column(Boolean, name=_tumor.fields.invasion_of_other_organs)
    pathological_tnm = Column(Boolean, name=_tumor.fields.pathological_tnm)
    pm = Column(Text, name=_tumor.fields.pm)                                                    # Var type currently undecided, probably Text
    pn = Column(Text, name=_tumor.fields.pn)                                                    # Var type currently undecided, probably Text
    pt = Column(Text, name=_tumor.fields.pt)                                                    # Var type currently undecided, probably Text
    reconstructed_tnm = Column(Text, name=_tumor.fields.reconstructed_tnm)                      # Probable
    resectability_tnm = Column(Text, name=_tumor.fields.resectability_tnm)                      # Probable
    tumor_location = Column(Text, name=_tumor.fields.tumor_location)
    tumor_size = Column(Text, name=_tumor.fields.tumor_size)

    clinical_tnm_raw_value = Column(Text, name=_tumor.fields.clinical_tnm_raw_value)
    combined_tnm_raw_value = Column(Text, name=_tumor.fields.combined_tnm_raw_value)                                # Probable
    histology_description_raw_value = Column(Text, name=_tumor.fields.histology_description_raw_value)
    histology_present_raw_value = Column(Text, name=_tumor.fields.histology_present_raw_value)
    invasion_of_other_organs_raw_value = Column(Text, name=_tumor.fields.invasion_of_other_organs_raw_value)
    pathological_tnm_raw_value = Column(Text, name=_tumor.fields.pathological_tnm_raw_value)
    pm_raw_value = Column(Text, name=_tumor.fields.pm_raw_value)                                                    # Var type currently undecided, probably Text
    pn_raw_value = Column(Text, name=_tumor.fields.pn_raw_value)                                                    # Var type currently undecided, probably Text
    pt_raw_value = Column(Text, name=_tumor.fields.pt_raw_value)                                                    # Var type currently undecided, probably Text
    reconstructed_tnm_raw_value = Column(Text, name=_tumor.fields.reconstructed_tnm_raw_value)                      # Probable
    resectability_tnm_raw_value = Column(Text, name=_tumor.fields.resectability_tnm_raw_value)                      # Probable
    tumor_location_raw_value = Column(Text, name=_tumor.fields.tumor_location_raw_value)
    tumor_size_raw_value = Column(Text, name=_tumor.fields.tumor_size_raw_value)

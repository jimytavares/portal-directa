# Generated by Django 4.2.10 on 2024-05-06 01:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('saude_farmacia', '0001_initial'),
        ('saude', '0002_initial'),
        ('comum', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('saude_atendimento', '0001_initial'),
        ('saude_cadastro', '0001_initial'),
        ('saude_enfermagem', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicacaoatendimento',
            name='lista_chamada_solicitacao',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='saude_enfermagem.listachamadasolicitacaoatendimento'),
        ),
        migrations.AddField(
            model_name='medicacaoatendimento',
            name='medicacao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='saude_farmacia.medicamento'),
        ),
        migrations.AddField(
            model_name='medicacaoatendimento',
            name='medico',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='medico_medicacao_atendomento_set', to='saude_cadastro.profissional'),
        ),
        migrations.AddField(
            model_name='listachamada',
            name='classificacao_risco',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='classificacao_risco_lista_chamada_set', to='saude_atendimento.classificacaorisco'),
        ),
        migrations.AddField(
            model_name='listachamada',
            name='medico',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='medico_lista_chamada_set', to='saude_cadastro.profissional'),
        ),
        migrations.AddField(
            model_name='listachamada',
            name='paciente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='paciente_lista_chamada_set', to='saude_atendimento.paciente'),
        ),
        migrations.AddField(
            model_name='listachamada',
            name='sala',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='sala_lista_chamada_set', to='saude_cadastro.sala'),
        ),
        migrations.AddField(
            model_name='listachamada',
            name='unidade_saude',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='saude.unidadesaude', verbose_name='Unidade de Saúde'),
        ),
        migrations.AddField(
            model_name='horariomedico',
            name='medico_horariomedico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='saude_cadastro.profissional', verbose_name='Médico'),
        ),
        migrations.AddField(
            model_name='historicoesperaatendimento',
            name='lista_chamada',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='saude_atendimento.listachamada'),
        ),
        migrations.AddField(
            model_name='historicalpaciente',
            name='anamnese_paciente',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='saude_atendimento.anamnesepaciente'),
        ),
        migrations.AddField(
            model_name='historicalpaciente',
            name='estado',
            field=models.ForeignKey(blank=True, db_constraint=False, help_text='Estado', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='comum.estado'),
        ),
        migrations.AddField(
            model_name='historicalpaciente',
            name='history_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historicalpaciente',
            name='municipio',
            field=smart_selects.db_fields.ChainedForeignKey(blank=True, chained_field='estado', chained_model_field='estado', db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='comum.municipio'),
        ),
        migrations.AddField(
            model_name='historicalpaciente',
            name='profissao',
            field=models.ForeignKey(blank=True, db_constraint=False, help_text='Profissão', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='saude_cadastro.profissao'),
        ),
        migrations.AddField(
            model_name='historicalpaciente',
            name='rg_uf',
            field=models.ForeignKey(blank=True, db_constraint=False, help_text='UF da emissão do RG', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='comum.estado'),
        ),
        migrations.AddField(
            model_name='historicalpaciente',
            name='unidade_saude',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='saude.unidadesaude', verbose_name='Unidade de Saúde'),
        ),
        migrations.AddField(
            model_name='historicallistachamada',
            name='classificacao_risco',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='saude_atendimento.classificacaorisco'),
        ),
        migrations.AddField(
            model_name='historicallistachamada',
            name='history_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historicallistachamada',
            name='medico',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='saude_cadastro.profissional'),
        ),
        migrations.AddField(
            model_name='historicallistachamada',
            name='paciente',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='saude_atendimento.paciente'),
        ),
        migrations.AddField(
            model_name='historicallistachamada',
            name='sala',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='saude_cadastro.sala'),
        ),
        migrations.AddField(
            model_name='historicallistachamada',
            name='unidade_saude',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='saude.unidadesaude', verbose_name='Unidade de Saúde'),
        ),
        migrations.AddField(
            model_name='historicalclassificacaorisco',
            name='boletim',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='saude_atendimento.boletimpaciente', verbose_name='Boletim'),
        ),
        migrations.AddField(
            model_name='historicalclassificacaorisco',
            name='history_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historicalclassificacaorisco',
            name='paciente',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='saude_atendimento.paciente'),
        ),
        migrations.AddField(
            model_name='historicalclassificacaorisco',
            name='tipo_classificacao_risco',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='saude_cadastro.tipoclassificacaorisco'),
        ),
        migrations.AddField(
            model_name='historicalboletimpaciente',
            name='history_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historicalboletimpaciente',
            name='paciente',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='saude_atendimento.paciente'),
        ),
        migrations.AddField(
            model_name='historicalboletimpaciente',
            name='profissional',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='saude_cadastro.profissional'),
        ),
        migrations.AddField(
            model_name='historicalboletimpaciente',
            name='unidade_saude',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='saude.unidadesaude'),
        ),
        migrations.AddField(
            model_name='historicalanamnesepaciente',
            name='history_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='fichareferenciaatendimento',
            name='atendimento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='saude_atendimento.atendimentomedico'),
        ),
        migrations.AddField(
            model_name='fichareferenciaatendimento',
            name='diagnosticos',
            field=models.ManyToManyField(blank=True, to='saude_atendimento.diagnosticoatendimento'),
        ),
        migrations.AddField(
            model_name='fichareferenciaatendimento',
            name='exames',
            field=models.ManyToManyField(blank=True, to='saude_atendimento.exameatendimento'),
        ),
        migrations.AddField(
            model_name='fichareferenciaatendimento',
            name='medicacoes',
            field=models.ManyToManyField(blank=True, to='saude_atendimento.medicacaoatendimento'),
        ),
        migrations.AddField(
            model_name='fichareferenciaatendimento',
            name='profissional',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='saude_cadastro.profissional'),
        ),
        migrations.AddField(
            model_name='exameatendimento',
            name='atendimento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='atendimento_exame_atendimento_set', to='saude_atendimento.atendimentomedico'),
        ),
        migrations.AddField(
            model_name='exameatendimento',
            name='exame',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='saude_cadastro.exame'),
        ),
        migrations.AddField(
            model_name='exameatendimento',
            name='lista_chamada_solicitacao',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='saude_enfermagem.listachamadasolicitacaoatendimento'),
        ),
        migrations.AddField(
            model_name='exameatendimento',
            name='medico_solicitante',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='medico_solicitante_exame_atendimento_set', to='saude_cadastro.profissional'),
        ),
        migrations.AddField(
            model_name='exameatendimento',
            name='profissional_responsavel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='profissional_responsavel_exame_atendimento_set', to='saude_cadastro.profissional'),
        ),
        migrations.AddField(
            model_name='evolucaoatendimento',
            name='atendimento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='atendimento_evolucao_atendimento_set', to='saude_atendimento.atendimentomedico'),
        ),
        migrations.AddField(
            model_name='evolucaoatendimento',
            name='profissional',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='saude_cadastro.profissional'),
        ),
        migrations.AddField(
            model_name='documentopaciente',
            name='paciente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='saude_atendimento.paciente'),
        ),
        migrations.AddField(
            model_name='documentopaciente',
            name='profissional',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='saude_cadastro.profissional'),
        ),
        migrations.AddField(
            model_name='diagnosticoatendimento',
            name='atendimento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='atendimento_diagnostico_atendimento_set', to='saude_atendimento.atendimentomedico'),
        ),
        migrations.AddField(
            model_name='diagnosticoatendimento',
            name='cid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cid_diagnostico_atendimento_set', to='saude_cadastro.cid'),
        ),
        migrations.AddField(
            model_name='diagnosticoatendimento',
            name='profissional',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='saude_cadastro.profissional'),
        ),
        migrations.AddField(
            model_name='classificacaorisco',
            name='boletim',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='boletim_classificacao_risco_set', to='saude_atendimento.boletimpaciente', verbose_name='Boletim'),
        ),
        migrations.AddField(
            model_name='classificacaorisco',
            name='paciente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paciente_classificacao_risco_set', to='saude_atendimento.paciente'),
        ),
        migrations.AddField(
            model_name='classificacaorisco',
            name='tipo_classificacao_risco',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='saude_cadastro.tipoclassificacaorisco'),
        ),
        migrations.AddField(
            model_name='boletimpaciente',
            name='paciente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='paciente_boletim_set', to='saude_atendimento.paciente'),
        ),
        migrations.AddField(
            model_name='boletimpaciente',
            name='profissional',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='profissional_boletim_paciente_set', to='saude_cadastro.profissional'),
        ),
        migrations.AddField(
            model_name='boletimpaciente',
            name='unidade_saude',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='saude.unidadesaude'),
        ),
        migrations.AddField(
            model_name='bloqueioagenda',
            name='medico_bloqueio_agenda',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='saude_cadastro.profissional', verbose_name='Médico'),
        ),
        migrations.AddField(
            model_name='atestadoatendimento',
            name='atendimento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='saude_atendimento.atendimentomedico'),
        ),
        migrations.AddField(
            model_name='atestadoatendimento',
            name='cid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='saude_cadastro.cid'),
        ),
        migrations.AddField(
            model_name='atestadoatendimento',
            name='profissional',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='saude_cadastro.profissional'),
        ),
        migrations.AddField(
            model_name='atendimentomedico',
            name='classificacao_risco',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='classificacao_risco_atendimento_medico_set', to='saude_atendimento.classificacaorisco'),
        ),
        migrations.AddField(
            model_name='atendimentomedico',
            name='lista_chamada',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='lista_chamada_atendimento_medico_set', to='saude_atendimento.listachamada'),
        ),
        migrations.AddField(
            model_name='atendimentomedico',
            name='paciente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='paciente_atendimento_medico_set', to='saude_atendimento.paciente'),
        ),
        migrations.AddField(
            model_name='atendimentomedico',
            name='profissionais',
            field=models.ManyToManyField(blank=True, to='saude_cadastro.profissional'),
        ),
        migrations.AddField(
            model_name='atendimentomedico',
            name='unidade_saude',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='saude.unidadesaude', verbose_name='Unidade de Saúde'),
        ),
        migrations.AddField(
            model_name='anamnesepaciente',
            name='alergias_medicamentosas',
            field=models.ManyToManyField(blank=True, related_name='alergias_medicamentosas', to='saude_farmacia.principioativo'),
        ),
        migrations.AddField(
            model_name='anamnesepaciente',
            name='antecedentes_patologicos_familiares',
            field=models.ManyToManyField(blank=True, related_name='antecedentes_patologicos_familiares', to='saude_cadastro.cid'),
        ),
        migrations.AddField(
            model_name='anamnesepaciente',
            name='antecedentes_patologicos_pessoais',
            field=models.ManyToManyField(blank=True, related_name='antecedentes_patologicos_pessoais', to='saude_cadastro.cid'),
        ),
        migrations.AddField(
            model_name='agendamentoconsultorio',
            name='agendado_por',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Agendado por'),
        ),
        migrations.AddField(
            model_name='agendamentoconsultorio',
            name='medico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='saude_cadastro.profissional', verbose_name='Médico'),
        ),
        migrations.AddField(
            model_name='agendamentoconsultorio',
            name='paciente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='saude_atendimento.paciente', verbose_name='Paciente'),
        ),
        migrations.AddField(
            model_name='agendamentoconsultorio',
            name='unidade_saude',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='saude.unidadesaude', verbose_name='Unidade de Saúde'),
        ),
    ]

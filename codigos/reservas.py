from django.db import IntegrityError, models, transaction


class Reserva(models.Model):
    horario = models.ForeignKey("Horario", on_delete=models.CASCADE)
    estudante = models.ForeignKey("Estudante", on_delete=models.CASCADE)
    data = models.DateField()
    assunto = models.CharField(max_length=200, blank=True)
    presente = models.BooleanField(null=True)

    class Meta:
        # Um horário só pode ter uma reserva em cada data (RF03).
        constraints = [
            models.UniqueConstraint(
                fields=["horario", "data"], name="reserva_unica_por_horario"
            )
        ]


class HorarioOcupado(Exception):
    """O horário foi reservado por outro estudante."""


def reservar(estudante, horario, data):
    """Cria a reserva ou lança HorarioOcupado se o horário já foi tomado."""
    try:
        with transaction.atomic():
            return Reserva.objects.create(
                estudante=estudante, horario=horario, data=data
            )
    except IntegrityError:
        # A restrição do banco impede reservas simultâneas no mesmo horário.
        raise HorarioOcupado(horario, data)

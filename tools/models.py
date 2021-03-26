from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
    """The Base model, with which we check the change of fields."""

    _old_values = {}

    class Meta:
        abstract = True

    @classmethod
    def from_db(cls, db, field_names, values):
        instance = super().from_db(db, field_names, values)
        instance._old_values = dict(zip(field_names, values))
        return instance


class BaseUpdatableModel(BaseModel):
    """
    The Base model, which to display the creation|update date,
    delete (bool) and the delete time.
    """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)

    removed_at = models.DateTimeField(blank=True, null=True, default=None)
    is_removed = models.BooleanField(default=False)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        """
        The methods saves the current deletion time, if don't have otherwise.
        """

        if self.is_removed and self.removed_at is None:
            self.removed_at = timezone.now()
        super().save(*args, **kwargs)


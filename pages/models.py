from django.db import models

# Create your models here.

class Post(models.Model):
	m_valve_type = models.CharField(max_length=100, default='empty')
	m_body_size = models.CharField(max_length=100, default='empty')
	m_body_material = models.CharField(max_length=100, default='empty')
	m_rating = models.CharField(max_length=100, default='empty')
	m_end_connections = models.CharField(max_length=100, default='empty')
	m_stem_material = models.CharField(max_length=100, default='empty')
	m_seat_material = models.CharField(max_length=100, default='empty')
	m_bonnet_bolting_material = models.CharField(max_length=100, default='empty')
	m_trim_type = models.CharField(max_length=100, default='empty')
	m_trim_size = models.CharField(max_length=100, default='empty')
	m_trim_material = models.CharField(max_length=100, default='empty')
	m_leakage_class = models.CharField(max_length=100, default='empty')
	m_fire_safe = models.CharField(max_length=100, default='empty')
	m_nace_requirement = models.CharField(max_length=100, default='empty')
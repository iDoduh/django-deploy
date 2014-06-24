from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from shop.models import FeaturePlugin as FeaturePluginModel
from shop.models import Plan, Feature, Carousel
from django.utils.translation import ugettext as _


class FeaturePlugin(CMSPluginBase):
    model = FeaturePluginModel # Model where data about this plugin is saved
    name = _("Feature Plugin") # Name of the plugin
    render_template = "shop/feature-plugin.html" # template to render the plugin with

    def render(self, context, instance, placeholder):
        context.update({"instance": instance})
        return context


plugin_pool.register_plugin(FeaturePlugin) # register the plugin


class FeatureListPlugin(CMSPluginBase):
    name = _("Features list") # Name of the plugin
    render_template = "shop/featurelist-plugin.html" # template to render the plugin with

    def render(self, context, instance, placeholder):
        context.update({"features": Feature.objects.filter(is_active=1)})
        return context


plugin_pool.register_plugin(FeatureListPlugin) # register the plugin


class PlansPlugin(CMSPluginBase):
    name = _("Plans Plugin") # Name of the plugin
    render_template = "shop/plans-plugin.html" # template to render the plugin with

    def render(self, context, instance, placeholder):
        context.update({"plans": Plan.objects.all()})
        return context


plugin_pool.register_plugin(PlansPlugin) # register the plugin


class CarouselPlugin(CMSPluginBase):
    name = _("Carousel Plugin")
    render_template = "shop/carousel-plugin.html" # template to render the plugin with

    def render(self, context, instance, placeholder):
        context.update({"carousel_list": Carousel.objects.all()})
        return context


plugin_pool.register_plugin(CarouselPlugin) # register the plugin
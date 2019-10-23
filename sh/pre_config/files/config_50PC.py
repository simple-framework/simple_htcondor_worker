from generic_helpers import get_dns_info, get_batch_dns_info
from models.config_file import ConfigFile


class WorkerConfig(ConfigFile):
    def __init__(self, output_file, augmented_site_level_config, execution_id):
        ConfigFile.__init__(self, output_file, augmented_site_level_config, execution_id)

    def add_static_parameters(self):
        super().add_static_parameters()
        self.static_category.add("Use ROLE: Execute\n")
        self.static_category.add_key_value("STARTER_ALLOW_RUNAS_OWNER", "false")
        self.static_category.add_key_value("EXECUTE_LOGIN_IS_DEDICATED", "true")

    def add_lightweight_component_queried_parameters(self):
        super().add_lightweight_component_queried_parameters()
        self.lightweight_component_queried_category.add_key_value_query("num_slots", "$.config.num_slots")

    def add_advanced_parameters(self):
        super().add_advanced_parameters()
        num_slots = self.lightweight_component['config']['num_slots']
        for slot in range(0, num_slots):
            self.advanced_category.add_key_value("SLOT{slot}_USER".format(slot=slot), "slot{slot}".format(slot=slot))
        execution_id = self.lightweight_component['execution_id']
        dns = get_dns_info(self.augmented_site_level_config, execution_id)
        allow_write = '.'.join((dns['container_ip'].split('.')[0:-2] + ['*']))
        self.advanced_category.add_key_value("allow_write", allow_write)
        batch_ip = get_batch_dns_info(self.augmented_site_level_config)['container_ip']
        self.advanced_category.add_key_value("condor_host", batch_ip)

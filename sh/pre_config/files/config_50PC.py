from models.config_file import ConfigFile


class WorkerConfig(ConfigFile):
    def __init__(self, output_file, augmented_site_level_config, execution_id):
        ConfigFile.__init__(self, output_file, augmented_site_level_config, execution_id)

    def add_static_parameters(self):
        super().add_static_parameters()
        self.static_category.add_key_value("Use Role", "Execute")
        self.static_category.add_key_value("ALLOW_WRITE","*")
        self.static_category.add_key_value("STARTER_ALLOW_RUNAS_OWNER", "false")
        self.static_category.add_key_value("EXECUTE_LOGIN_IS_DEDICATED", "true")

    def add_lightweight_component_queried_parameters(self):
        super().add_lightweight_component_queried_parameters()
        self.lightweight_component_queried_category.add_key_value_query("CONDOR_HOST", "$.deploy.node")

    def add_advanced_parameters(self):
        super().add_advanced_parameters()
        num_slots = self.lightweight_component['config']['user_slots']
        for slot in range(0, num_slots):
            self.advanced_category.add_key_value("SLOT{slot}_USER".format(slot=slot), "slot{slot}".format(slot=slot))

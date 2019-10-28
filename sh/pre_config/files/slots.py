from config_file import ConfigFile


class Slots(ConfigFile):
    def __init__(self, output_file, augmented_site_level_config, execution_id):
        ConfigFile.__init__(self, output_file, augmented_site_level_config, execution_id)

    def add_advanced_parameters(self):
        super().add_advanced_parameters()
        num_slots = self.lightweight_component['config']['num_slots']
        for slot in range(0, num_slots):
            self.advanced_category.add("slot{slot}\n".format(slot=slot))
        self.advanced_category.add("simple")

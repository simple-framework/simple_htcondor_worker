import yaml
import argparse

from models.config_file import ConfigFile
from categories.config_50PC import WorkerConfig


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--site_config', help="Compiled Site Level Configuration YAML file")
    parser.add_argument('--execution_id', help="ID of lightweight component")
    parser.add_argument('--output_dir', help="Output directory")
    args = parser.parse_args()
    return {
        'augmented_site_level_config_file': args.site_config,
        'execution_id': args.execution_id,
        'output_dir': args.output_dir
    }


if __name__ == "__main__":
    args = parse_args()
    execution_id = args['execution_id']
    augmented_site_level_config_file = args['augmented_site_level_config_file']
    augmented_site_level_config_file = open(augmented_site_level_config_file, 'r')
    augmented_site_level_config = yaml.safe_load(augmented_site_level_config_file)
    output_dir = args['output_dir']

    print(augmented_site_level_config)

    config_50PC = ConfigFile("{output_dir}/50PC.config".format(output_dir=output_dir),augmented_site_level_config)
    config_50PC.add_categories(WorkerConfig("config_50PC", augmented_site_level_config, execution_id).get_categories())

    config_50PC.generate_output_file()

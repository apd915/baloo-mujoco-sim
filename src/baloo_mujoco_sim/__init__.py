#TODO: would be nice to run this as part of the install process...

import subprocess
from pathlib import Path as path

import mujoco


def find_xml_files_in_assets(package_name):
    """
    Find all xml files in the assets folder of the package.
    :param package_name: name of the package
    :return: list of xml files
    """
    assets_path = path(__file__).parent / 'assets'
    xml_files = list(assets_path.glob('*.xml'))
    return [str(xml_file) for xml_file in xml_files]


def load_mujoco_plugins():
    """
    Load the custom MuJoCo plugins required by the Baloo model.
    """

    # __file__ is:
    # baloo-mujoco-sim/src/baloo_mujoco_sim/__init__.py
    #
    # parents[0] = baloo_mujoco_sim
    # parents[1] = src
    # parents[2] = baloo-mujoco-sim
    repo_root = path(__file__).resolve().parents[2]

    plugins = [
        repo_root
        / "plugin"
        / "build"
        / "joint_angle_estimator"
        / "libjoint_angle_estimator.so",

        repo_root
        / "plugin"
        / "build"
        / "ruckig_actuator"
        / "libRuckigActuator.so",
    ]

    for plugin in plugins:
        if not plugin.exists():
            raise FileNotFoundError(
                f"Required MuJoCo plugin not found:\n{plugin}"
            )

        try:
            print(f"Loading MuJoCo plugin: {plugin}")
            mujoco.mj_loadPluginLibrary(str(plugin))
        except mujoco.FatalError as e:
            if "already registered" in str(e):
                pass
            else:
                raise e


# Load plugins when baloo_mujoco_sim is imported.
# This must happen before loading any XML that references them.
load_mujoco_plugins()

# Example usage
package_name = 'baloo_mujoco_sim'
xml_files = find_xml_files_in_assets(package_name)

if xml_files:
    XML_PATH = xml_files[0]
else:
    #there is not xml file. So we need to generate it.
    print("No xml model found. Automatically generating xml file...")

    script = path(__file__).parent / "utils/generate_baloo_xml.py"

    res = subprocess.run(['python', script], capture_output=True, text=True)

    if res.returncode == 0:
        print(res.stdout)
        xml_files = find_xml_files_in_assets(package_name)
        XML_PATH = xml_files[0]
        print(f"Generated xml file: {XML_PATH}")
    else:
        print(res.stderr)
        raise Exception("Error while generating xml file")

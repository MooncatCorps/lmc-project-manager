import mooncat.pm.mc_data as mcd
import pathlib as pl
import os, sys, shutil
import sysconfig

def perform_installation(args: list[str], data: dict, dev: bool) -> bool:
    lang = mcd.get_property("development.lang", data)

    if not lang:
        sys.stderr.write("Could not determine project language\n")
        sys.stderr.write("Consider placing it in your .mooncat.toml")
        return False

    match lang:
        case "python":
            return install_python(data, dev)

    return True

def install_python(data: dict, dev: bool) -> bool:
    project_name = mcd.get_property("project.name", data)

    if not project_name:
        sys.stderr.write("Could not determine project name\n")
        sys.stderr.write("Consider placing it in your .mooncat.toml")
        return False

    print(f"[INSTALL] Project: {project_name}")

    lib_spath = get_lib_source_path("python")
    lib_ipath = get_lib_install_path("python")
    lib_tpath = set_up_project_install_dir(lib_ipath, project_name)
    print(f"[INSTALL] Location: {lib_tpath}")

    print("[INSTALL] Clearing old files")
    remove_or_unlink_dir(lib_tpath)

    print("[INSTALL] Inserting new files")
    copy_or_link_dir(lib_spath, lib_tpath, dev)

    return True

#
# Util
#

def set_up_project_install_dir(libpath: pl.Path, project_name: str) -> pl.Path:
    path = libpath/"mooncat"/project_name
    os.makedirs(path, exist_ok = True)
    return path

def remove_or_unlink_dir(path: pl.Path):
    if path.is_symlink():
        os.unlink(path)
    elif path.is_dir():
        shutil.rmtree(path)

def copy_or_link_dir(path_from: pl.Path, path_to: pl.Path, should_link: bool):
    if should_link:
        os.symlink(path_from, path_to, target_is_directory = True)
    else:
        os.makedirs(path_to, exist_ok = True)
        shutil.copytree(path_from, path_to, dirs_exist_ok = True)

#
# Lang Specific
#

def get_lib_source_path(lang: str) -> pl.Path:
    val = pl.Path("")
    match lang:
        case "python":
            val = pl.Path(os.getcwd())/"modules"

    if not val.exists():
        os.makedirs(val)

    return val


def get_lib_install_path(lang: str) -> pl.Path:
    val = pl.Path("")
    match lang:
        case "python":
            val = pl.Path(sysconfig.get_paths()["purelib"])

    if not val.exists():
        os.makedirs(val)

    return val


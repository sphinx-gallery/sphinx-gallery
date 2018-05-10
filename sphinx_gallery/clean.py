from argparse import ArgumentParser
import os.path
import shutil
import subprocess
import sys


if sys.version_info < (3,):
    def exec_(_code_, _globs_=None, _locs_=None):
        """Execute code in a namespace."""
        if _globs_ is None:
            frame = sys._getframe(1)
            _globs_ = frame.f_globals
            if _locs_ is None:
                _locs_ = frame.f_locals
            del frame
        elif _locs_ is None:
            _locs_ = _globs_
        exec("""exec _code_ in _globs_, _locs_""")
else:
    import builtins
    exec_ = builtins.exec


def main():
    parser = ArgumentParser(
        description=
        "Clean intermediate files generated by sphinx-gallery, and call "
        "'python -msphinx -M clean' with the same arguments.")
    parser.add_argument("sourcedir")
    parser.add_argument("builddir")
    args, _ = parser.parse_known_args()
    d = {}
    with open(os.path.join(args.sourcedir, "conf.py")) as conf_file:
        exec_(conf_file.read(), d)
    sg_conf = d["sphinx_gallery_conf"]
    for path in sg_conf["gallery_dirs"]:
        shutil.rmtree(os.path.join(args.sourcedir, path), ignore_errors=True)
    shutil.rmtree(os.path.join(args.sourcedir, sg_conf["backreferences_dir"]),
                  ignore_errors=True)
    subprocess.check_call(
        [sys.executable, "-msphinx", "-M", "clean"] + sys.argv[1:])


if __name__ == "__main__":
    main()

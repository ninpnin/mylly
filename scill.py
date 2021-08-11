#!/usr/local/bin/python3
from pathlib import Path

def mill_header():
    return """import mill._, scalalib._, scalanativelib._
import mill.scalanativelib.api.ReleaseMode\n\n"""

def mill_body(name, scala_version="2.13.4"):
    body = """object %s extends ScalaModule {
  def scalaVersion = \"%s\"
  //def logLevel = NativeLogLevel.Info // optional
  def releaseMode = ReleaseMode.ReleaseFull // optional
}""" % (name, scala_version)
    return body

def main():
    p = Path(".")
    print("Init scala project for mill")
    print("in the current folder:", p.absolute())

    package_name = input("Please provide package name: ")
    print("Package name:", package_name)

    root = p / package_name
    print(root)
    root.mkdir(parents=True)

    build_sc = root / "build.sc"
    build_sc.touch()
    build_sc = build_sc.open(mode='w')
    build_sc_content = mill_header() + mill_body(package_name)
    build_sc.write(build_sc_content)
    build_sc.close()

    pkg = root / package_name
    pkg.mkdir(parents=True)
    pkg_src = pkg / "src"
    pkg_src.mkdir(parents=True)
    pkg_src_pkg = pkg_src / package_name
    pkg_src_pkg.mkdir(parents=True)


if __name__ == '__main__':
    main()
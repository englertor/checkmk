load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")


def freetds(version_str, sha256):
    http_archive(
        name="freetds",
        build_file="@omd_packages//packages/freetds:BUILD.freetds.bazel",
        url="https://www.freetds.org/files/stable/freetds-" + version_str + ".tar.gz",
        sha256=sha256,
        strip_prefix="freetds-" + version_str,
    )

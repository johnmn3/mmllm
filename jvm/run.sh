#!/usr/bin/env bash
# Run the JVM port without the Clojure CLI: plain java -cp over pinned jars.
# Jars land in jvm/.jars on first run (Maven Central). Usage:
#   jvm/run.sh -m mmllm.jvm.m1-check
set -euo pipefail
cd "$(dirname "$0")/.."   # repo root — code uses repo-relative paths

JARS_DIR="jvm/.jars"
mkdir -p "$JARS_DIR"
declare -A GAV=(
  [clojure-1.12.0.jar]="org/clojure/clojure/1.12.0/clojure-1.12.0.jar"
  [spec.alpha-0.5.238.jar]="org/clojure/spec.alpha/0.5.238/spec.alpha-0.5.238.jar"
  [core.specs.alpha-0.4.74.jar]="org/clojure/core.specs.alpha/0.4.74/core.specs.alpha-0.4.74.jar"
)
for jar in "${!GAV[@]}"; do
  [ -f "$JARS_DIR/$jar" ] || curl -sSf -o "$JARS_DIR/$jar" \
    "https://repo1.maven.org/maven2/${GAV[$jar]}"
done

CP="jvm/src:jvm/resources:$(ls "$JARS_DIR"/*.jar | tr '\n' ':')"
exec java -XX:+UseParallelGC -Xmx4g -cp "$CP" clojure.main "$@"

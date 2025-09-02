bazel build --config=jav8 //...

## Helpers

bazel build //core:failsafe
bazel build //modules/okhttp

To create maven_install.json: (maven_install.json should NOT be used at the time):

```
bazel run @maven//:pin
```

bazel query @maven//:all --output=build

## Relevant documentation

https://github.com/bazel-contrib/rules_jvm_external?tab=readme-ov-file#generated-targets

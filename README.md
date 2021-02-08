# em-bug-upload

Simple flask server to save uploaded bug reports.

## Installation instructions

### For development

We use flask with auto-reload, set up with the source directory mounted correctly.

```
$ docker-compose -f docker-compose.dev.yml up
```

You can then edit the source code in `/src` and the app should reload automatically

### For production

```
$ docker-compose up
```

You can also copy-paste it into an existing docker-compose file. In that case,
you can remove the `external` tag.  A full explanation of `docker-compose`
settings is beyond the scope of this project.

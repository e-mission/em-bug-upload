# em-bug-upload

Simple flask server to save uploaded bug reports.

## Installation instructions

### For development

We use flask with auto-reload, set up with the source directory mounted correctly.

```
$ docker-compose -f docker-compose.dev.yml up
```

You can then edit the source code in `/src` and the app should reload automatically
As documented in the docker-compose, the dev server is available at http://localhost:5647/phonelogs

However, it only supports `POST`, so it is not accessible via the browser and you are expected to get a 405 error.

### For production

```
$ docker-compose up
```

You can copy-paste it into an existing docker-compose file. In that case, you
can remove the `network` entry to have it use the existing network.

You can also use it as a separate `docker-compose.yml` file. In that case, you
would use an external network.

```
 networks:
   emission:
+    external:
+      name: <main-docker-compose-network>
```

This even works with an ngnix proxy by removing the port mapping and adding
`VIRTUAL_HOST` entries

```
 services:
   uploader:
     build: .
-    ports:
-      # LOGS in numbers
-      - "5647:8080"
     volumes:
       - ./phonelogs/:/phonelogs
+    environment:
+      - VIRTUAL_HOST=host.domain
+      - LETSENCRYPT_HOST=host.domain
     networks:
       - emission
```

A full explanation of `docker-compose` settings is beyond the scope of this
project.

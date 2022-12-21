# MongoDB

|                |                                       |
| -------------- | ------------------------------------- |
| Name           | MongoDB                           |
| Version        | v1.0.0                                |
| DockerHub | [weevenetwork/mongodb](https://hub.docker.com/r/weevenetwork/mongodb) |
| Authors        | Jakub Grzelak                    |

- [MongoDB](#mongodb)
  - [Description](#description)
  - [Environment Variables](#environment-variables)
    - [Module Specific](#module-specific)
    - [Set by the weeve Agent on the edge-node](#set-by-the-weeve-agent-on-the-edge-node)
  - [Dependencies](#dependencies)
  - [Input](#input)
  - [Output](#output)

## Description

Write data to your selected MongoDB database and collection. When generating MongoDB Atlas URI please select `MongoDB Drivers` > `Python` > `3.12 or later`. If you need assist with getting your URI refer to [MongoDB documentation](https://www.mongodb.com/docs/atlas/tutorial/connect-to-your-cluster/).

## Environment Variables

### Module Specific

The following module configurations can be provided in a data service designer section on weeve platform:

| Name                 | Environment Variables     | type     | Description                                              |
| -------------------- | ------------------------- | -------- | -------------------------------------------------------- |
| MongoDB URI    | MONGO_URI         | string   | URI address of your MongoDB or your MongoDB Atlas.            |
| Database Name    | DATABASE_NAME         | string  | Name of the database to write data to.            |
| Collection Name    | COLLECTION_NAME         | string  | Name of the collection in the selected database to write data to.            |


### Set by the weeve Agent on the edge-node

Other features required for establishing the inter-container communication between modules in a data service are set by weeve agent.

| Environment Variables | type   | Description                                    |
| --------------------- | ------ | ---------------------------------------------- |
| MODULE_NAME           | string | Name of the module                             |
| MODULE_TYPE           | string | Type of the module (Input, Processing, Output)  |
| INGRESS_HOST          | string | Host to which data will be received            |
| INGRESS_PORT          | string | Port to which data will be received            |

## Dependencies

```txt
bottle
pymongo[srv]
```

## Input

Input to this module is:

* JSON body single object, example:

```json
{
   "temperature": 13,
   "volume": 13
}
```

* array of JSON body objects, example:

```json
[
    {
        "temperature": 13,
        "volume": 13
    },
    {
        "temperature": 23,
        "volume": 1
    }
]
```

## Output

Output of this module is:

Inserted data to the selected database and collection in the MongoDB.

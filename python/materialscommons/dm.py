class User(object):
    def __init__(self):
        pass

    def schema():
        _schema = {
            "title" : "User",
            "type" : "object",
            "properties" : {
                "id" : {"type": "string"},
                "apikey" : {
                    "description" : "User apikey for webservice calls",
                    "type" : "string"
                },   
                "createdOn" : {"type" : "date-time"},
                "lastModified" : {"type" : "date-time"},
                "name" : {
                    "description" : "username, as in jdoe",
                    "type" : "string"
                },
                "passwordHash" : {
                    "description" : "Hash of users password",
                    "type" : "string"
                },
                "contact" : {
                    "description" : "Embedded Contact object",
                    "type" : "object"
                },
                "notes" : {
                    "description" : "List of Notes objects",
                    "type" : "array",
                    "minimum" : 0,
                    "items": {"type" : "object"}
                }
            }
        }
        return _schema

class Note(object):
    def __init__(self):
        pass

    def schema():
        _schema = {
            "type" : "object",
            "properties": {
                "id" : {"type" : "string"},
                "createdBy" : {
                    "description" : "Id of user who created note",
                    "type" : "string"
                },
                "createdOn" : { "type" : "date-time"},
                "note" : {
                    "description" : "The text for the entry",
                    "type" : "string"
                }
            }
        }
        return _schema

class Project(object):
    def __init__(self):
        pass

    def schema():
        _schema = {
            "type" : "object",
            "description" : "",
            "properties" : {
                "id" : {"type" : "string"},
                "name" : {"type" : "string"},
                "description" : { "type" : "string"},
                "dataDir" : {
                    "description" : "id of root dataDir",
                    "type" : "string"
                },
                "owner" : {"type" : "string"},
                "createdOn" : {"type" : "date-time"},
                "lastModified" : {"type" : "date-time"},
                "notes" : {
                    "description" : "List of Notes objects",
                    "type" : "array",
                    "minimum" : 0,
                    "items": {"type" : "object"}
                },
                "tags" : {
                    "description" : "List of GlobalTag Ids",
                    "type": "array",
                    "minimum" : 0,
                    "items" : {"type" : "string"}
                },
                "reviews" : {
                    "description" : "List of Review Ids",
                    "type" : "array",
                    "minimum" : 0,
                    "items" : {"type" : "string"}
                }
            }
        }
        return _schema

class GlobalTag(object):
    def __init__(self):
        pass

    def schema():
        _schema = {
            "description" : "Tags that are global to the system",
            "type" : "object",
            "properties" : {
                "id" : {
                    "description" : "Because the name is unique, the name is the id",
                    "type" : "string"
                },
                "description" : {"type" : "string"},
                "notes" : {
                    "description" : "List of Notes objects",
                    "type" : "array",
                    "minimum" : 0,
                    "items": {"type" : "object"}
                },
            }
        }
        return _schema

class UserTag(object):
    def __init__(self):
        pass

    def schema():
        _schema = {
            "description" : "Tags that are global to the system",
            "type" : "object",
            "properties" : {
                "id" : {
                    "description" : "Unlike global tags, user tags do not have unique names",
                    "type" : "string"
                },
                "name" : {"type" : "string"},
                "user" : {
                    "description" : "Id of user owning this tag",
                    "type" : "string"
                },
                "description" : {"type" : "string"},
                "notes" : {
                    "description" : "List of Notes objects",
                    "type" : "array",
                    "minimum" : 0,
                    "items": {"type" : "object"}
                },
            }
        }
        return _schema

class Machine(object):
    def __init__(self):
        pass

    def schema():
        _schema = {
            "description" : "hardware such as a computer, microscope, etc... where you generated data",
            "type" : "object",
            "properties" : {
                "id" : {"type" : "string"},
                "name" : {
                    "description" : "machine name, eg 'flux'",
                    "type" : "hostname"
                },
                "fullname": {
                    "description" : "machine long name, eg flux-log.engin.umich.edu",
                    "type": "hostname"
                },
                "contact" : {
                    "description" : "Embedded Contact object",
                    "type" : "object"
                },
                "notes" : {
                    "description" : "List of Notes objects",
                    "type" : "array",
                    "minimum" : 0,
                    "items": {"type" : "object"}
                }
            }
        }
        return _schema

class Contact(object):
    def __init__(self):
        pass

    def schema():
        _schema = {
            "description" : "Embedded object, not a database table",
            "type" : "object",
            "properties" : {
                "fullname" : {"type" : "string"},
                "email" : {"type" : "email"},
                "phone" : {"type" : "string"},
                "website" : {"type" : "uri"},
                "avatar" : {
                    "description" : "http or file reference for picture",
                    "type" : "uri"
                }, 
                "description" : {
                    "description" : "Contact description/bio",
                    "type" : "string"
                },
                "affiliation" : {
                    "description" : "Contact affiliation, eg University of Michigan",
                    "type" : "string"
                },
                "notes" : {
                    "description" : "List of Notes objects",
                    "type" : "array",
                    "minimum" : 0,
                    "items": {"type" : "object"}
                },       
            }
        }
        return _schema

class UserGroup(object):
    def __init__(self):
        pass

    def schema():
        _schema = {
            "description" : "",
            "type" : "object",
            "properties" : {
                "id" : {"type" : "string"},
                "creatdOn" : {"type" : "date-time"},
                "lastModified" : {"type" : "date-time"},
                "owner" : {
                    "description" : "The Id for the user who created the group",
                    "type" : "string"
                },
                "name" : {"type" : "string"},
                "users" : {
                    "description" : "List of user (ids) who are in the group",
                    "type" : "array",
                    "minimum" : 0,
                    "items" : {"type" : "string"}
                }
            }
        }
        return _schema

class Process(object):
    def __init__(self):
        pass

    def schema():
        _schema = {
            "description" : "",
            "type" : "object",
            "properties" : {
                "id" : {"type" : "string"},
                "name" : {
                    "description" : "Name given by user",
                    "type" : "string"
                },
                "createdBy" : {
                    "description" : "The id of user who created the process",
                    "type" : "string"
                },
                "machine" : {
                    "description" : "id of machine process was performed on",
                    "type" : "string"
                },
                "processType" : {
                    "description" : "Type of process, eg 'VASP', 'GCMC', etc...",
                    "type" : "string"
                },
                "version" : {"type" : "string"},
                "parent" : {
                # What is this?
                    "description:" : "Parent process id this process was based on",
                    "type" : "string"
                },
                "notes" : {
                    "description" : "List of Notes objects",
                    "type" : "array",
                    "minimum" : 0,
                    "items": {"type" : "object"}
                },
                "inputDataFiles" : {
                    "description" : "List of input DataFile ids",
                    "type" : "array",
                    "minimum" : 0,
                    "items" : {"type" : "string"}
                },
                "outputDataFiles" : {
                    "description" : "List of output DataFile ids",
                    "type" : "array",
                    "minimum" : 0,
                    "items" : {"type" : "string"}
                },
                "inputDataParams" : {
                    "description" : "List of input DataParam ids"
                    "type" : "array",
                    "minimum" : 0,
                    "items" : {"type" : "string"}
                },
                "outputDataParams" : {
                    "description" : "List of output DataParam ids"
                    "type" : "array",
                    "minimum" : 0,
                    "items" : {"type" : "string"}
                },
                "runs" : {
                    "description" : "List of runs within this Process",
                    "type" : "array",
                    "minimum" : 0,
                    "items" : {
                        "type" : "object",
                        "properties" : {
                            "startTime" : {"type" : "date-time"},
                            "stopTime" : {"type" : "date-time"},
                            "errorMessages" : {
                                "description" : "List of error messages",
                                "type" : "array",
                                "minimum" : 0,
                                "items" : {"type" : "string"}
                            },
                        },
                },
                "citations" : {
                    # What to do with this - separate into an object?
                    "description" : "List of citations",
                    "type" : "array",
                    "minimum" : 0,
                    "items" : {"type" : "string"}                    
                },
                "status" : {"enum" : ["aborted", "successful", "running", "cancelled", "queued"]}
            }
        }
        return _schema


class DataParam(object):
    def __init__(self):
        pass

    def schema():
        _schema = {
            "description" : "",
            "type" : "object",
            "properties" : {
                "id" : {"type" : "string"},
                "params" : {
                    "description" : "key/value pairs",
                    "type" : "object",
                }
            }
        }
        return _schema

class DataDir(object):
    def __init__(self):
        pass

    def schema():
        _schema = {
            "description" : "",
            "type" : "object",
            "properties" : {
                "id" : {"type" : "string"},
                "access" : {
                    "description" : "Is it private or public",
                    # Are there other access types?
                    "enum" : ["private", "public"]
                },
                "dataFiles" : {
                    "description" : "List of DataFile Ids",
                    "type" : "string"
                },
                "createdOn" : {"type" : "date-time"},
                "lastModified" : {"type" : "date-time"},
                "markedForReview" : {"type" : "boolean"},
                "myTags" : {
                    "description" : "List of ids for tags user privately created",
                    "type" : "array",
                    "minimum" : 0,
                    "items" : {"type" : "string"}
                },
                "tags" : {
                    "description" : "List of ids for global tags",
                    "type" : "array",
                    "minimum" : 0,
                    "items" : {"type" : "string"}
                },
                "name" : {"type" : "string"},
                "owner" : {
                    "description" : "Id of user who owns this object",
                    "type" : "string"
                },
                "parentDataDir" : {
                    "description" : "parent data dir id",
                    "type" : "string"
                },
                "reviews" : {
                    "description" : "List of review object ids",
                    "type" : "array",
                    "minimum" : 0,
                    "items" : {"type", "string"}
                }
            }
        }
        return _schema

class Review(object):
    def __init__(self):
        pass

    def schema():
        _schema = {
            "description" : "",
            "type" : "object",
            "properties" : {
                "id" : {"type" : "string"},
                "who" : {
                    "description" : "Who should conduct the review",
                    "type" : "string"
                },
                "owner" : {
                    "description" : "Who requested the review",
                    "type" : "string"
                },
                "note" : {
                    "description" : "A note describing what you want out of the review",
                    "type" : "string"
                },
                "type" {
                    "description" : "The type of review requested.",
                    # Are there other types?
                    "enum" : ["dataparam", "datafile", "datadir", "project"]
                },
                "itemName" : {
                    "description" : "Name of item the review is for",
                    "type" : "string"
                },
                "itemId" : {
                    "description" : "Id of item to review",
                    "type" : "string"
                },
                "markedOn" : {
                    "description" : "Date item was marked for review",
                    "type" : "date-time"
                }
            }
        }
        return _schema

class DataFile(object):
    def __init__(self):
        pass

    def schema():
        _schema = {
            "description" : "",
            "type" : "object",
            "properties" : {
                "id" : {"type" : "string"},
                "access" : {
                    "description" : "Is it private or public",
                    # Are there other access types?
                    "enum" : ["private", "public"]
                },
                "checksum" : {
                    "description" : "file checksum",
                    "type" : "string"
                },
                "size" : {"type" : "integer"},
                "dataDirs" : {
                    "description" : "List of dataDir ids this file can be found in",
                    "type" : "array",
                    "minimum" : 1,
                    "items" : {"type" : "string"}
                },
                "createdOn" : {"type" : "date-time"},
                "lastModified" : {"type" : "date-time"},
                "markedForReview" : {"type" : "boolean"},
                "myTags" : {
                    "description" : "List of ids for tags user privately created",
                    "type" : "array",
                    "minimum" : 0,
                    "items" : {"type" : "string"}
                },
                "tags" : {
                    "description" : "List of ids for global tags",
                    "type" : "array",
                    "minimum" : 0,
                    "items" : {"type" : "string"}
                },
                "name" : {"type" : "string"},
                "owner" : {
                    "description" : "Id of user who owns this object",
                    "type" : "string"
                },
                "description" : {"type" : "string"},
                "location" : {
                    "description" : "Location on disk, relative to some base",
                    "type" : "string"
                },
                "mediaType" : {
                    "description" : "Type of file as determined by Tika",
                    "type" : "string"
                },
                "metaTags" : {
                    "description" : "Dictionary of key/value pairs 'name'/'value'",
                    "type" : "array",
                    "items" : {"type" : "object"}
                },
                "name" : {"type" : "string"},
                "reviews" : {
                    "description" : "List of review object ids",
                    "type" : "array",
                    "minimum" : 0,
                    "items" : {"type", "string"}
                },
                "notes" : {
                    "description" : "List of Notes objects",
                    "type" : "array",
                    "minimum" : 0,
                    "items": {"type" : "object"}
                },
                "text" : {
                    "description" : "Text extracted from document",
                    # We may not need to store this
                    "type" : "string"
                }
            }
        }
        return _schema

class DataSet(object):
    def __init__(self):
        pass

    def schema():
        _schema = {
            "description" : "",
            "type" : "object",
            "properties" : {
                "id" : {"type" : "string"},
                "name": {"type" : "string"},
                "owner" : {
                    "description" : "User id who created this DataSet"
                    "type" : "string"
                },
                "notes" : {
                    "description" : "List of Notes objects",
                    "type" : "array",
                    "minimum" : 0,
                    "items": {"type" : "object"}
                },
                "dataFiles" : {
                    "description" : "List of DataFile ids",
                    "type" : "array",
                    "minimum" : 0,
                    "items" : {"type" : "string"}
                },
                "dataParams" : {
                    "description" : "List of DataParam ids",
                    "type" : "array",
                    "minimum" : 0,
                    "items" : {"type" : "string"}
                },
                "createdOn" : {"type" : "date-time"}
            }
        }
        return _schema

class News(object):
    def __init__(self):
        pass

    def schema():
        _schema = {
            "description" : "",
            "type" : "object",
            "properties" : {
                "id" : {"type" : "string"},
                "date" : {"type" : "date-time"},
                "title" : {"type" : "string"},
                "body" : {"type" : "string"}
            }
        }
        return _schema

class UDJob(object):
    def __init__(self):
        pass

    def schema():
        _schema = {
            # Needs work
            "description" : "Upload/Download Job",
            "type" : "object",
            "properties" : {
                "id" : {"type" : "string"},
                "name" : {"type" : "string"},
                "type" : {
                    "description" : "Type of job",
                    "enum" : ["upload", "download"]
                },
                "createdBy" : {
                    "description" : "User id who created",
                    "type" : "string"
                },
                "host" : {
                    "description" : "Host to do upload/download to",
                    "type" : "ipv4",
                },
                "path" : {
                    "description" : "Path to load from/to",
                    "type" : "string"
                },
                "status" : {
                    "enum" : ["TBD"]
                },
                "note" : {"type" : "string"},
                "submittedOn" : {"type" : "date-time"},
                "dataDir" : {
                    "description" : "DataDir Id to upload to/download from"
                    "type" : "string"
                }
                "logs" : {
                    "description" : "List of Log entries"
                    "type" : "array",
                    "minimum" : 0,
                    "items" : {
                        "type" : "object",
                        "properties" : {
                            "tstamp" : {"type" : "date-time"},
                            "entry" : {"type" : "string"}
                        }
                    }
                }
            }
        }
        return _schema

class Template(object):
    def __init__(self):
        pass

    def schema():
        _schema = {
            "description" : "Template for various types - TBD",
            "type" : "object",
            "properties" : {
                "id" : {"type" : "string"},
            }
        }
        return _schema

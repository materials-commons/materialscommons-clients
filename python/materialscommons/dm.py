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
                "created_on" : {"type" : "date-time"},
                "last_modified" : {"type" : "date-time"},
                "email" : {"type" : "email"},
                "fullname" : {"type" : "string"},
                "password_hash" : {
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
                "created_by" : {
                    "description" : "Id of user who created note",
                    "type" : "string"
                },
                "created_on" : { "type" : "date-time"},
                "key" : { "type" : "string"},
                "note" : {
                    "description" : "The text for the entry",
                    "type" : "string"
                },
                "units" : {"type" : "string"}
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
                "datadir" : {
                    "description" : "id of root dataDir",
                    "type" : "string"
                },
                "owner" : {"type" : "string"},
                "created_on" : {"type" : "date-time"},
                "last_modified" : {"type" : "date-time"},
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
                # Needs a list of items that it is tagged to and moved out of DataDir, and DataFile
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
                "created_on" : {"type" : "date-time"},
                "last_modified" : {"type" : "date-time"},
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
                "created_on" : {"type" : "date-time"},
                "last_modified" : {"type" : "date-time"},
                "created_by" : {
                    "description" : "The id of user who created the process",
                    "type" : "string"
                },
                "machine" : {
                    "description" : "id of machine process was performed on",
                    "type" : "string"
                },
                "process_type" : {
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
                "input_dataitems" : {
                    "description" : "List of DataItem ids",
                    "type" : "array",
                    "minimum" : 0,
                    "items" : {"type" : "string"}
                },
                "input_datasets" : {
                    "description" : "List of DataSet ids",
                    "type" : "array",
                    "minimum" : 0,
                    "items" : {"type" : "string"}
                },
                "output_dataitems" : {
                    "description" : "List of DataItem ids",
                    "type" : "array",
                    "minimum" : 0,
                    "items" : {"type" : "string"}
                },
                "output_datasets" : {
                    "description" : "List of DataSet ids",
                    "type" : "array",
                    "minimum" : 0,
                    "items" : {"type" : "string"}
                },
                "runs" : {
                    "description" : "List of Run objects",
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
                    "description" : "List of Citation objects",
                    "type" : "array",
                    "minimum" : 0,
                    "items" : {"type" : "object"}                    
                },
                "status" : {"enum" : ["aborted", "successful", "running", "cancelled", "queued"]}
                
                # For prov, also want:
                #   created_by_name, 
                #   machine_name, 
                #   input_dataitem_names, 
                #   input_dataset_names, 
                #   output_dataitem_names, 
                #   output_dataset_names
            }
        }
        return _schema

class Run(object):
    def __init__(self):
        pass

    def schema():
        _schema = {
            "description" : "Start time, stop time, and error messages associated with one run of a Process.",
            "type" : "object",
            "properties" : {
                "started" : {"type" : "date-time"},
                "stopped" : {"type" : "date-time"}
                "error_messages" : {
                    "type" : "array",
                    "minimum" : 0,
                    "items" : {"type" : "string"}
                }
            }
        }
        return _schema

class Citation(object):
    def __init__(self):
        pass

    def schema():
        _schema = {
            "description" : "",
            "type" : "object",
            "properties" : {
                # what should go here? BibTex string? or BibTex data items?
                "text" : {"type" : "string"}
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
                "name" : {"type" : "string"},
                "owner" : {
                    "description" : "Id of user who owns this object",
                    "type" : "string"
                },
                "access" : {
                    "description" : "Is it private or public",
                    # Are there other access types?
                    "enum" : ["private", "public"]
                },
                "dataitems" : {
                    "description" : "List of DataItem Ids",
                    "type" : "string"
                },
                "created_on" : {"type" : "date-time"},
                "last_modified" : {"type" : "date-time"},
                "marked_for_review" : {"type" : "boolean"},
                "my_tags" : {
                    # must be filtered for a particular user
                    "description" : "List of ids for tags users privately create",
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
                "parent_datadir" : {
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
                "item_name" : {
                    "description" : "Name of item the review is for",
                    "type" : "string"
                },
                "item_id" : {
                    "description" : "Id of item to review",
                    "type" : "string"
                },
                "marked_on" : {
                    "description" : "Date item was marked for review",
                    "type" : "date-time"
                }
            }
        }
        return _schema

class DataItem(object):
    def __init__(self):
        pass

    def schema():
        _schema = {
            "description" : "A data file and/or parameters",
            "type" : "object",
            "properties" : {
                
                ## Static items -----------------------------------------------
                ##   These must not change after creating the DataItem
                ##   Provenance is unchanging, trustworthy
                ##   The file this points at should not change, though it's location might
                
                "id" : {"type" : "string"},
                "checksum" : {
                    "description" : "file checksum",
                    "type" : "string"
                },
                "size" : {"type" : "integer"},
                "created_on" : {"type" : "date-time"}, # is the file or the DataItem object? I assume object?
                "owner" : {
                    "description" : "Id of user who owns this object",
                    "type" : "string"
                },
                "machine" : {
                    "description" : "ID of machine dataitem was created with",
                    "type" : "string"
                },
                "media_type" : {
                    "description" : "Type of file as determined by Tika",
                    "type" : "string"
                },
                "params" : {
                    "description" : "List of Notes objects used as parameters",
                    "type" : "array",
                    "minimum" : 0,
                    "items": {"type" : "object"}
                },
                
                
                ## Mutable items -----------------------------------------------
                ##   These may change after creating the DataItem
                ##   Should not use for provenance
                
                "name" : {"type" : "string"},
                "description" : {"type" : "string"},
                "last_modified" : {"type" : "date-time"}, # is the file or the DataItem object? I assume object? 
                "location" : {
                    "description" : "Location on disk, relative to some base",
                    "type" : "string"
                },
                "access" : {
                    "description" : "Is it private or public",
                    # Are there other access types?
                    "enum" : ["private", "public"]
                },
                "datadirs" : {
                    "description" : "List of dataDir ids this file can be found in",
                    "type" : "array",
                    "minimum" : 1,
                    "items" : {"type" : "string"}
                },
                "creator" : {
                    "description" : "The ID of the Process that created this",
                    "type" : "string"
                },
                "my_tags" : {
                    # must be filtered for a particular user
                    "description" : "List of ids for tags users privately create",
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
                "meta_tags" : {
                    "description" : "Dictionary of key/value pairs 'name'/'value'",
                    "type" : "array",
                    "items" : {"type" : "object"}
                },
                "marked_for_review" : {"type" : "boolean"},
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
                
                # For prov, also want:
                #   owner_name, 
                #   machine_name, 
                #   input_dataitem_names, 
                #   input_dataset_names, 
                #   output_dataitem_names, 
                #   output_dataset_names
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
                
                ## Static items -----------------------------------------------
                ##   These must not change after creating the DataSet
                ##   Provenance is unchanging, trustworthy
                ##   The file this points at should not change, though it's location might
                
                "id" : {"type" : "string"},
                "name": {"type" : "string"},
                "created_on" : {"type" : "date-time"},
                "dataitems" : {
                    "description" : "List of DataFile ids",
                    "type" : "array",
                    "minimum" : 0,
                    "items" : {"type" : "string"}
                },
                "owner" : {
                    "description" : "User id who created this DataSet"
                    "type" : "string"
                },
                
                
                ## Mutable items -----------------------------------------------
                ##   These may change after creating the DataItem
                ##   Should not use for provenance
                
                "notes" : {
                    "description" : "List of Notes objects",
                    "type" : "array",
                    "minimum" : 0,
                    "items": {"type" : "object"}
                }
                
                # For prov, also want:
                #   dataitem_names, 
                #   owner_name
                
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
                "created_by" : {
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
                "submitted_on" : {"type" : "date-time"},
                "datadir" : {
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

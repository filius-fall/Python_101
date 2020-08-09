# dictLogConfig={
#     "version":1,
#     "handlers":{
#         "fileHandler":{
#             "class":"logging.FileHandler",
#             "formatter":"myFormatter",
#             "filename":"config2.log"
#         }
#     },
#     "loggers":{
#         "exampleapp":{
#             "handlers":["fileHandler"],
#             "level":"INFO",

#         },
#         "formatters":{
#             "myFormatter":{
#                 "format":"%(asctime)s - %(name)s - %(levelname)s - %(message)s"
#             }
#         }
        
#     }
# }
import logging
import logging.config


def log_file():
    dictLogConfig = {
        "version":1,
        "handlers":{
            "fileHandler":{
                "class":"logging.FileHandler",
                "formatter":"myFormatter",
                "filename":"config2.log"
            }
        },
        "loggers":{
            "exampleApp":{
                "handlers":["fileHandler"],
                "level":"INFO",
            }
        },
        "formatters":{
            "myFormatter":{
                "format":"%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            }
        }
        
    }
    return dictLogConfig
    
    # logging.config.dictConfig(dictLogConfig)
    # logger = logging.getLogger("exampleApp")

    # logger.info("Program started")
    # result = 7
    # logger.info("Done!")

if __name__ == "__main__":
    log_file()
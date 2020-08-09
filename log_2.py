import logging
import mod

# def main():
#     logging.basicConfig(filename="logs/mod_log.log", level=logging.INFO)
#     logging.info("Program started")
#     result=mod.add(2,3)
#     logging.info("program ended")


def main():
    logger=logging.getLogger('example')
    logger.setLevel(logging.INFO)

    fh=logging.FileHandler("logs/mog_log2.log")
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)

    logger.addHandler(fh)

    logger.info("Program Has Started")
    result=mod.add(3,5)
    logger.info("Program Executed")

if __name__ == "__main__":
    main()
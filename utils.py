def process_filenos(filenos, fmt="%04d"):
    return [fmt % fileno for fileno in filenos]
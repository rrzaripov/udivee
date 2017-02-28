# -*- coding: utf-8 -*-
from dicom import read_file


class DicomFile:
    def __init__(self):
        pass

    @staticmethod
    def read(filename):
        # TODO: implement more intelligent way to read files
        ds = read_file(filename, stop_before_pixels=True, force=True)
        result = dict()
        for attr in ds.dir():
            result[attr] = ds.data_element(attr).value
        return ds

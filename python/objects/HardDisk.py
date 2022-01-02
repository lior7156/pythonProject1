class HardDisk:
    def __init__(self):
        self.t_space = 100
        self.occ_space = 0
        self.files_num = 0

    def show(self):
        print(f"total space in GB: {self.t_space}\n"
              f"occupied space in GB: {self.occ_space}\n"
              f"number of files: {self.files_num}")

    def freespace(self):
        freespace = self.t_space - self.occ_space
        return freespace

    def addfile(self, file_size):
        if file_size > self.t_space - self.occ_space:
            print("the file is too large")
        else:
            self.occ_space = self.occ_space + file_size
            self.files_num += 1
            print("the file han been transferred")

    def delfile(self, file_size):
        if self.occ_space <= file_size:
            self.occ_space = 0
        else:
            self.occ_space = self.occ_space - file_size
            self.files_num -= 1

class Material:
    def __init__(self, mat_name :str, mat_price :float ) -> None:
         self.mat_name = str.lower(mat_name)
         self.mat_price = mat_price

    def file_format(self) -> str:
        return f"{self.mat_name},{self.mat_price}\n"
    
    def __str__(self) -> str:
        return f"Material [{self.mat_name},{self.mat_price}]"

    def __repr__(self) -> str:
        return f"<materials.Material object [{str.title(self.mat_name)},{self.mat_price}]>"

    def equals(self, other) -> bool:
        return (self.mat_name == other.mat_name) and (self.mat_price == other.mat_price)

    def __eq__(self, other: object) -> bool:
        return (str.lower(self.mat_name) == str.lower(other.mat_name)) and (self.mat_price == other.mat_name)
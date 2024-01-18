from stl import mesh

stl_path = 'D:/cansat/UI/New GUI/3d/assem.stl'

stl_model = mesh.Mesh.from_file(stl_path)

vectors = stl_model.vectors
normals = stl_model.normals

print(len(vectors))
print(len(normals))
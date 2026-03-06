class hospital:
    def operation():
        print("This is a hospital")
class doctor(hospital):
    def doc():
        print("Doctor works at hospital")
class patient(doctor):
    def pat():
        print("Patient treated by doc at hospital")

p = patient
p.pat()
p.doc()
p.operation()

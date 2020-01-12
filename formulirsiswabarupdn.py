import Tkinter

root = Tkinter.Tk()
root.configure(bg="white")
root.title("Formulir Siswa")
root.geometry("500x500")

lbl_title = Tkinter.Label(root, text="Formulir Siswa Baru SMK PDN", bg="white")
lbl_title.grid(row=0, column=1, columnspan=3)

lbl_ID_Pendaftaran = Tkinter.Label(root, text="ID PENDAFTARAN", bg="white")
lbl_ID_Pendaftaran.grid(row=1, column=1)

lbl_tip = Tkinter.Label(root, text=":", bg="white")
lbl_tip.grid(row=1, column=2)

txt_input_ID_Pendaftaran = Tkinter.Entry(root, width=30)
txt_input_ID_Pendaftaran.grid(row=1, column=3)
txt_input_ID_Pendaftaran.focus()

lbl_Nama_Lengkap = Tkinter.Label(root, text="NAMA LENGKAP", bg="white")
lbl_Nama_Lengkap.grid(row=2, column=1)

lbl_tnl = Tkinter.Label(root, text=":", bg="white")
lbl_tnl.grid(row=2, column=2)

txt_input_Nama_Lengkap = Tkinter.Entry(root, width=30)
txt_input_Nama_Lengkap.grid(row=2, column=3)

lbl_Tempat_Lahir = Tkinter.Label(root, text="TEMPAT LAHIR", bg="white")
lbl_Tempat_Lahir.grid(row=3, column=1)

lbl_ttl = Tkinter.Label(root, text=":", bg="white")
lbl_ttl.grid(row=3, column=2)

txt_input_Tempat_Lahir = Tkinter.Entry(root, width=30)
txt_input_Tempat_Lahir.grid(row=3, column=3)

lbl_Tanggal_Lahir = Tkinter.Label(root, text="TANGGAL LAHIR", bg="white")
lbl_Tanggal_Lahir.grid(row=4, column=1)

lbl_tgl = Tkinter.Label(root, text=":", bg="white")
lbl_tgl.grid(row=4, column=2)

txt_input_Tanggal_Lahir = Tkinter.Entry(root, width=30)
txt_input_Tanggal_Lahir.grid(row=4, column=3)

lbl_Jenis_Kelamin = Tkinter.Label(root, text="JENIS KELAMIN", bg="white")
lbl_Jenis_Kelamin.grid(row=5, column=1)

lbl_tjk = Tkinter.Label(root, text=":", bg="white")
lbl_tjk.grid(row=5, column=2)

rad_laki = Tkinter.Radiobutton(root, text='LAKI-LAKI', bg="white")
rad_laki.grid(row=5, column=3)
rad_perempuan = Tkinter.Radiobutton(root, text='PEREMPUAN', bg="white")
rad_perempuan.grid(row=6, column=3)

lbl_Asal_Sekolah = Tkinter.Label(root, text="ASAL SEKOLAH", bg="white")
lbl_Asal_Sekolah.grid(row=7, column=1)

lbl_tas = Tkinter.Label(root, text=":", bg="white")
lbl_tas.grid(row=7, column=2)

txt_input_Asal_Sekolah = Tkinter.Entry(root, width=30)
txt_input_Asal_Sekolah.grid(row=7, column=3)

lbl_Alamat = Tkinter.Label(root, text="ALAMAT", bg="white")
lbl_Alamat.grid(row=8, column=1)

lbl_tal = Tkinter.Label(root, text=":", bg="white")
lbl_tal.grid(row=8, column=2)

txt_input_Alamat = Tkinter.Entry(root, width=30)
txt_input_Alamat.grid(row=8, column=3)

btn_Save = Tkinter.Button(root, text="SIMPAN")
btn_Save.grid(row=11, column=1)

btn_Perbarui = Tkinter.Button(root, text="PERBARUI")
btn_Perbarui.grid(row=11, column=2)

btn_Hapus = Tkinter.Button(root, text="HAPUS")
btn_Hapus.grid(row=11, column=3)

btn_Keluar = Tkinter.Button(root, text="KELUAR")
btn_Keluar.grid(row=11, column=4)


root.mainloop()

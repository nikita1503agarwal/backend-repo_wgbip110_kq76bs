"""
Database Schemas for PPDB SMK Bakti Nusantara 666

Each Pydantic model maps to a MongoDB collection (lowercased class name):
- Account -> "account"
- Applicant -> "applicant"

Edit the fields marked with [EDITABLE] to customize labels/requirements.
"""
from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List

# === [EDITABLE] Akun untuk autentikasi ===
class Account(BaseModel):
    name: str = Field(..., description="Nama lengkap")
    email: EmailStr = Field(..., description="Email aktif untuk login")
    password_hash: str = Field(..., description="Hash kata sandi (disimpan ter-enkripsi)")
    role: str = Field("applicant", description="Peran pengguna: applicant/admin")
    phone: Optional[str] = Field(None, description="Nomor HP")

# === [EDITABLE] Data pendaftar (form pendaftaran) ===
class Applicant(BaseModel):
    account_email: EmailStr = Field(..., description="Email akun yang terkait")
    full_name: str = Field(..., description="Nama lengkap sesuai ijazah")
    nisn: str = Field(..., description="Nomor Induk Siswa Nasional")
    major_choice: str = Field(..., description="Pilihan jurusan utama")
    secondary_choice: Optional[str] = Field(None, description="Pilihan jurusan cadangan")
    address: Optional[str] = Field(None, description="Alamat lengkap")
    school_origin: Optional[str] = Field(None, description="Asal sekolah")
    guardian_name: Optional[str] = Field(None, description="Nama orang tua/wali")
    guardian_phone: Optional[str] = Field(None, description="Nomor HP orang tua/wali")
    documents: Optional[List[str]] = Field(default=None, description="URL dokumen yang diunggah")
    status: str = Field("submitted", description="Status pendaftaran: draft/submitted/verified/accepted/rejected")

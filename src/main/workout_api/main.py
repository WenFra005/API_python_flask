from fastapi import FastAPI, HTTPException, Query
from fastapi_pagination import Pagination, paginate
from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel
from sqlalchemy.exc import IntegrityError

# Configuração do banco de dados
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# Modelo de dados
class Atleta(Base):
    __tablename__ = "atletas"
    id = Column(Integer, Sequence("atleta_id_seq"), primary_key=True)
    nome = Column(String, index=True)
    cpf = Column(String, unique=True, index=True)
    centro_treinamento = Column(String)
    categoria = Column(String)


# Criação das tabelas
Base.metadata.create_all(bind=engine)


# Pydantic model
class AtletaCreate(BaseModel):
    nome: str
    cpf: str
    centro_treinamento: str
    categoria: str


class AtletaResponse(BaseModel):
    nome: str
    centro_treinamento: str
    categoria: str


app = FastAPI()


@app.post("/atletas/", response_model=AtletaResponse)
def create_atleta(atleta: AtletaCreate, db: Session = SessionLocal()):
    new_atleta = Atleta(**atleta.dict())
    try:
        db.add(new_atleta)
        db.commit()
        db.refresh(new_atleta)
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=303,
            detail=f"Já existe um atleta cadastrado com o cpf: {atleta.cpf}",
        )
    return AtletaResponse(
        nome=new_atleta.nome,
        centro_treinamento=new_atleta.centro_treinamento,
        categoria=new_atleta.categoria,
    )


@app.get("/atletas/", response_model=Pagination[AtletaResponse])
def get_atletas(
    limit: int = Query(10), offset: int = Query(0), db: Session = SessionLocal()
):
    atletas = db.query(Atleta).offset(offset).limit(limit).all()
    return paginate(atletas)

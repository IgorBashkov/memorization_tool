from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///flashcard.db?check_same_thread=False')
Base = declarative_base()


class FlashCards(Base):
    __tablename__ = 'flashcard'
    id = Column(Integer, primary_key=True)
    question = Column(String)
    answer = Column(String)


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


def results():
    return session.query(FlashCards).all()


def add_cards(question, answer):
    session.add(FlashCards(question=question, answer=answer))
    session.commit()


def delete_card(card_id):
    entry = session.query(FlashCards).get(card_id)
    session.delete(entry)
    session.commit()


def edit_card(card_id, question, answer):
    if question and answer:
        entry = session.query(FlashCards).get(card_id)
        entry.answer = answer
        entry.question = question
        session.commit()


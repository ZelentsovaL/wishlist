from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    userId: Mapped[Integer] = mapped_column(Integer, primary_key=True, index=True)
    userNickname: Mapped[str] = mapped_column()
    userPassword: Mapped[str] = mapped_column()

    profile: Mapped["Profile"] = relationship("Profile", back_populates="user")

class Profile(Base):
    __tablename__ = "profiles"

    profileId: Mapped[Integer] = mapped_column(Integer, primary_key=True, index=True)
    userId: Mapped[Integer] = mapped_column(ForeignKey("users.userId"))
    userSurname: Mapped[str] = mapped_column()
    userName: Mapped[str] = mapped_column()
    userPatronymic: Mapped[str] = mapped_column(nullable=True)
    
    user: Mapped["User"] = relationship("User", back_populates="profile")

class ListOfPresents(Base):
    __tablename__ = "list_of_presents"

    listOfPresentId: Mapped[Integer] = mapped_column(Integer, primary_key=True, index=True)
    presentShortName: Mapped[str] = mapped_column()
    presentsLLongName: Mapped[str] = mapped_column()
    presentDescription: Mapped[str] = mapped_column()

class Present(Base):
    __tablename__ = "presents"

    presentId: Mapped[Integer] = mapped_column(Integer, primary_key=True, index=True)
    presentName: Mapped[str] = mapped_column()
    presentDescription: Mapped[str] = mapped_column()
    presentPrice: Mapped[float] = mapped_column()
    presentCurrencyId: Mapped[int] = mapped_column(ForeignKey("currencies.currencyId"))
    presentUrl: Mapped[str] = mapped_column()
    presentListId: Mapped[int] = mapped_column(nullable=True)
    secretPresent: Mapped[bool] = mapped_column()
    presentListOfPresentId: Mapped[int] = mapped_column(ForeignKey("list_of_presents.listOfPresentId"))
    presentCurrency: Mapped["Currency"] = relationship("Currency", back_populates="presents")

class Currency(Base):
    __tablename__ = "currencies"

    currencyId: Mapped[Integer] = mapped_column(Integer, primary_key=True, index=True)
    currencyName: Mapped[str] = mapped_column()
    currencySymbol: Mapped[str] = mapped_column()
    presents: Mapped["Present"] = relationship("Present", back_populates="currency")
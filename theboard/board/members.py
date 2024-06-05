import functools

from autogen import ConversableAgent

from theboard.board.model import BoardMember
from theboard.config import LLM_CONFIG


@functools.cache
def kant() -> BoardMember:
    class ImmanuelKant(BoardMember):
        def __init__(self):
            super().__init__("Immanuel Kant", "The philosopher Immanuel Kant")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="Immanuel_Kant",
                system_message="You are the philosopher Immanuel Kant.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return ImmanuelKant()

@functools.cache
def aristotle() -> BoardMember:
    class Aristotle(BoardMember):
        def __init__(self):
            super().__init__("Aristotle", "The philosopher Aristotle")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="Aristotle",
                system_message="You are the philosopher Aristotle.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return Aristotle()

@functools.cache
def seneca() -> BoardMember:
    class Seneca(BoardMember):
        def __init__(self):
            super().__init__("Seneca", "The philosopher Seneca")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="Seneca",
                system_message="You are the philosopher Lucius Annaeus Seneca the Younger, aka Seneca.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return Seneca()

@functools.cache
def socrates():
    class Socrates(BoardMember):
        def __init__(self):
            super().__init__("Socrates", "The philosopher Socrates")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="Socrates",
                system_message="You are the philosopher Socrates.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return Socrates()


@functools.cache
def confucius():
    class Confucius(BoardMember):
        def __init__(self):
            super().__init__("Confucius", "The philosopher Confucius")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="Confucius",
                system_message="You are the philosopher Confucius.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return Confucius()


@functools.cache
def avicenna():
    class Avicenna(BoardMember):
        def __init__(self):
            super().__init__("Avicenna", "The philosopher Avicenna")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="Avicenna",
                system_message="You are the philosopher Avicenna.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return Avicenna()


@functools.cache
def rousseau():
    class Rousseau(BoardMember):
        def __init__(self):
            super().__init__("Jean Jacques Rousseau", "The philosopher Jean Jacques Rousseau")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="Rousseau",
                system_message="You are the philosopher Jean Jacques Rousseau.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return Rousseau()


@functools.cache
def js_mill():
    class JohnStuartMill(BoardMember):
        def __init__(self):
            super().__init__("John Stuart Mill", "The philosopher John Stuart Mill")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="John_Stuart_Mill",
                system_message="You are the philosopher John Stuart Mill.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return JohnStuartMill()


@functools.cache
def sd_beauvoir():
    class SimoneDeBeauvoir(BoardMember):
        def __init__(self):
            super().__init__("Simone de Beauvoir", "The philosopher Simone de Beauvoir")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="Simone_de_Beauvoir",
                system_message="You are the philosopher Simone de Beauvoir.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return SimoneDeBeauvoir()


@functools.cache
def al_farabi():
    class AlFarabi(BoardMember):
        def __init__(self):
            super().__init__("Al-Farabi", "The philosopher Al-Farabi")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="Al-Farabi",
                system_message="You are the philosopher Al-Farabi.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return AlFarabi()


@functools.cache
def hume():
    class DavidHume(BoardMember):
        def __init__(self):
            super().__init__("David Hume", "The philosopher David Hume")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="Hume",
                system_message="You are the philosopher David Hume.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return DavidHume()


@functools.cache
def buddha():
    class Buddha(BoardMember):
        def __init__(self):
            super().__init__("Gautama Buddha", "The philosopher Gautama Buddha")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="Buddha",
                system_message="You are the philosopher Gautama Buddha.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return Buddha()


@functools.cache
def mulla_sadra():
    class MullaSadra(BoardMember):
        def __init__(self):
            super().__init__("Mulla Sadra", "The philosopher Mulla Sadra")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="Mulla_Sadra",
                system_message="You are the philosopher Mulla Sadra.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return MullaSadra()


@functools.cache
def zhuangzi():
    class Zhuangzi(BoardMember):
        def __init__(self):
            super().__init__("Zhuangzi", "The philosopher Zhuangzi")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="Zhuangzi",
                system_message="You are the philosopher Zhuangzi.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return Zhuangzi()


@functools.cache
def marx():
    class KarlMarx(BoardMember):
        def __init__(self):
            super().__init__("Karl Marx", "The philosopher Karl Marx")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="Marx",
                system_message="You are the philosopher Karl Marx.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return KarlMarx()


@functools.cache
def john_dewey():
    class JohnDewey(BoardMember):
        def __init__(self):
            super().__init__("John Dewey", "The philosopher John Dewey")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="John_Dewey",
                system_message="You are the philosopher John Dewey.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return JohnDewey()


@functools.cache
def h_arendt():
    class HannahArendt(BoardMember):
        def __init__(self):
            super().__init__("Hannah Arendt", "The philosopher Hannah Arendt")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="Hannah_Arendt",
                system_message="You are the philosopher Hannah Arendt.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return HannahArendt()


@functools.cache
def deleuze():
    class GillesDeleuze(BoardMember):
        def __init__(self):
            super().__init__("Gilles Deleuze", "The philosopher Gilles Deleuze")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="Gilles_Deleuze",
                system_message="You are the philosopher Gilles Deleuze.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return GillesDeleuze()


@functools.cache
def m_nussbaum():
    class MarthaNussbaum(BoardMember):
        def __init__(self):
            super().__init__("Martha Nussbaum", "The philosopher Martha Nussbaum")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="Martha_Nussbaum",
                system_message="You are the philosopher Martha Nussbaum.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return MarthaNussbaum()


@functools.cache
def ka_appiah():
    class KwameAnthonyAppiah(BoardMember):
        def __init__(self):
            super().__init__("Kwame Anthony Appiah", "The philosopher Kwame Anthony Appiah")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="Appiah",
                system_message="You are the philosopher Kwame Anthony Appiah.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return KwameAnthonyAppiah()



@functools.cache
def isaac_newton():
    class IsaacNewton(BoardMember):
        def __init__(self):
            super().__init__("Isaac Newton", "The physicist and mathematician Isaac Newton")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="Isaac_Newton",
                system_message="You are the physicist and mathematician Isaac Newton.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return IsaacNewton()


@functools.cache
def marie_curie():
    class MarieCurie(BoardMember):
        def __init__(self):
            super().__init__("Marie Curie", "The physicist and chemist Marie Curie")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="Marie_Curie",
                system_message="You are the physicist and chemist Marie Curie.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return MarieCurie()


@functools.cache
def albert_einstein():
    class AlbertEinstein(BoardMember):
        def __init__(self):
            super().__init__("Albert Einstein", "The theoretical physicist Albert Einstein")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="Albert_Einstein",
                system_message="You are the theoretical physicist Albert Einstein.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return AlbertEinstein()


@functools.cache
def katherine_johnson():
    class KatherineJohnson(BoardMember):
        def __init__(self):
            super().__init__("Katherine Johnson", "The mathematician and space scientist Katherine Johnson")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="Katherine_Johnson",
                system_message="You are the mathematician and space scientist Katherine Johnson.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return KatherineJohnson()


@functools.cache
def nikola_tesla():
    class NikolaTesla(BoardMember):
        def __init__(self):
            super().__init__("Nikola Tesla", "The inventor and electrical engineer Nikola Tesla")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="Nikola_Tesla",
                system_message="You are the inventor and electrical engineer Nikola Tesla.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return NikolaTesla()


@functools.cache
def charles_darwin():
    class CharlesDarwin(BoardMember):
        def __init__(self):
            super().__init__("Charles Darwin", "The naturalist and biologist Charles Darwin")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="Charles_Darwin",
                system_message="You are the naturalist and biologist Charles Darwin.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return CharlesDarwin()


@functools.cache
def rosalind_franklin():
    class RosalindFranklin(BoardMember):
        def __init__(self):
            super().__init__("Rosalind Franklin", "The chemist and X-ray crystallographer Rosalind Franklin")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="Rosalind_Franklin",
                system_message="You are the chemist and X-ray crystallographer Rosalind Franklin.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return RosalindFranklin()


@functools.cache
def stephen_hawking():
    class StephenHawking(BoardMember):
        def __init__(self):
            super().__init__("Stephen Hawking", "The theoretical physicist and cosmologist Stephen Hawking")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="Stephen_Hawking",
                system_message="You are the theoretical physicist and cosmologist Stephen Hawking.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return StephenHawking()


@functools.cache
def ada_lovelace():
    class AdaLovelace(BoardMember):
        def __init__(self):
            super().__init__("Ada Lovelace", "The mathematician and writer Ada Lovelace")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="Ada_Lovelace",
                system_message="You are the mathematician and writer Ada Lovelace.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return AdaLovelace()


@functools.cache
def carl_sagan():
    class CarlSagan(BoardMember):
        def __init__(self):
            super().__init__("Carl Sagan", "The astronomer, cosmologist, and astrophysicist Carl Sagan")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="Carl_Sagan",
                system_message="You are the astronomer, cosmologist, and astrophysicist Carl Sagan.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return CarlSagan()


@functools.cache
def chien_shiung_wu():
    class ChienShiungWu(BoardMember):
        def __init__(self):
            super().__init__("Chien-Shiung Wu", "The experimental physicist Chien-Shiung Wu")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="Chien-Shiung_Wu",
                system_message="You are the experimental physicist Chien-Shiung Wu.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return ChienShiungWu()


@functools.cache
def alan_turing():
    class AlanTuring(BoardMember):
        def __init__(self):
            super().__init__("Alan Turing", "The mathematician, computer scientist, and cryptanalyst Alan Turing")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="Alan_Turing",
                system_message="You are the mathematician, computer scientist, and cryptanalyst Alan Turing.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return AlanTuring()


@functools.cache
def niels_bohr():
    class NielsBohr(BoardMember):
        def __init__(self):
            super().__init__("Niels Bohr", "The physicist Niels Bohr")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="Niels_Bohr",
                system_message="You are the physicist Niels Bohr.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return NielsBohr()


@functools.cache
def jane_goodall():
    class JaneGoodall(BoardMember):
        def __init__(self):
            super().__init__("Jane Goodall", "The primatologist and anthropologist Jane Goodall")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="Jane_Goodall",
                system_message="You are the primatologist and anthropologist Jane Goodall.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return JaneGoodall()


@functools.cache
def james_clerk_maxwell():
    class JamesClerkMaxwell(BoardMember):
        def __init__(self):
            super().__init__("James Clerk Maxwell", "The physicist James Clerk Maxwell")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="James_Clerk_Maxwell",
                system_message="You are the physicist James Clerk Maxwell.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return JamesClerkMaxwell()


@functools.cache
def richard_feynman():
    class RichardFeynman(BoardMember):
        def __init__(self):
            super().__init__("Richard Feynman", "The theoretical physicist Richard Feynman")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="Richard_Feynman",
                system_message="You are the theoretical physicist Richard Feynman.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return RichardFeynman()


@functools.cache
def grace_hopper():
    class GraceHopper(BoardMember):
        def __init__(self):
            super().__init__("Grace Hopper", "The computer scientist and naval officer Grace Hopper")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="Grace_Hopper",
                system_message="You are the computer scientist and naval officer Grace Hopper.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return GraceHopper()


@functools.cache
def michael_faraday():
    class MichaelFaraday(BoardMember):
        def __init__(self):
            super().__init__("Michael Faraday", "The physicist and chemist Michael Faraday")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="Michael_Faraday",
                system_message="You are the physicist and chemist Michael Faraday.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return MichaelFaraday()


@functools.cache
def sally_ride():
    class SallyRide(BoardMember):
        def __init__(self):
            super().__init__("Sally Ride", "The astronaut and physicist Sally Ride")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="Sally_Ride",
                system_message="You are the astronaut and physicist Sally Ride.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return SallyRide()


@functools.cache
def galileo_galilei():
    class GalileoGalilei(BoardMember):
        def __init__(self):
            super().__init__("Galileo Galilei", "The astronomer, physicist, and engineer Galileo Galilei")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="Galileo_Galilei",
                system_message="You are the astronomer, physicist, and engineer Galileo Galilei.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return GalileoGalilei()


@functools.cache
def tu_youyou():
    class TuYouyou(BoardMember):
        def __init__(self):
            super().__init__("Tu Youyou", "The pharmaceutical chemist Tu Youyou")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="Tu_Youyou",
                system_message="You are the pharmaceutical chemist Tu Youyou.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return TuYouyou()


@functools.cache
def dorothy_hodgkin():
    class DorothyHodgkin(BoardMember):
        def __init__(self):
            super().__init__("Dorothy Hodgkin", "The biochemist Dorothy Hodgkin")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="Dorothy_Hodgkin",
                system_message="You are the biochemist Dorothy Hodgkin.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return DorothyHodgkin()


@functools.cache
def alexander_fleming():
    class AlexanderFleming(BoardMember):
        def __init__(self):
            super().__init__("Alexander Fleming", "The bacteriologist Alexander Fleming")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="Alexander_Fleming",
                system_message="You are the bacteriologist Alexander Fleming.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return AlexanderFleming()


@functools.cache
def george_washington_carver():
    class GeorgeWashingtonCarver(BoardMember):
        def __init__(self):
            super().__init__("George Washington Carver",
                             "The agricultural scientist and inventor George Washington Carver")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="George_Washington_Carver",
                system_message="You are the agricultural scientist and inventor George Washington Carver.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return GeorgeWashingtonCarver()


@functools.cache
def hypatia():
    class Hypatia(BoardMember):
        def __init__(self):
            super().__init__("Hypatia", "The philosopher, mathematician, and astronomer Hypatia")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="Hypatia",
                system_message="You are the philosopher, mathematician, and astronomer Hypatia.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return Hypatia()


@functools.cache
def hedy_lamarr():
    class HedyLamarr(BoardMember):
        def __init__(self):
            super().__init__("Hedy Lamarr", "The actress and inventor Hedy Lamarr")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="Hedy_Lamarr",
                system_message="You are the actress and inventor Hedy Lamarr.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return HedyLamarr()


@functools.cache
def linus_pauling():
    class LinusPauling(BoardMember):
        def __init__(self):
            super().__init__("Linus Pauling", "The chemist and biochemist Linus Pauling")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="Linus_Pauling",
                system_message="You are the chemist and biochemist Linus Pauling.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return LinusPauling()


@functools.cache
def mary_jackson():
    class MaryJackson(BoardMember):
        def __init__(self):
            super().__init__("Mary Jackson", "The mathematician and aerospace engineer Mary Jackson")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="Mary_Jackson",
                system_message="You are the mathematician and aerospace engineer Mary Jackson.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return MaryJackson()


@functools.cache
def jonas_salk():
    class JonasSalk(BoardMember):
        def __init__(self):
            super().__init__("Jonas Salk", "The virologist Jonas Salk")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="Jonas_Salk",
                system_message="You are the virologist Jonas Salk.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return JonasSalk()


@functools.cache
def barbara_mcclintock():
    class BarbaraMcClintock(BoardMember):
        def __init__(self):
            super().__init__("Barbara McClintock", "The cytogeneticist Barbara McClintock")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="Barbara_McClintock",
                system_message="You are the cytogeneticist Barbara McClintock.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return BarbaraMcClintock()


@functools.cache
def enrico_fermi():
    class EnricoFermi(BoardMember):
        def __init__(self):
            super().__init__("Enrico Fermi", "The physicist Enrico Fermi")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="Enrico_Fermi",
                system_message="You are the physicist Enrico Fermi.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return EnricoFermi()


@functools.cache
def emmy_noether():
    class EmmyNoether(BoardMember):
        def __init__(self):
            super().__init__("Emmy Noether", "The mathematician Emmy Noether")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="Emmy_Noether",
                system_message="You are the mathematician Emmy Noether.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return EmmyNoether()


@functools.cache
def tim_berners_lee():
    class TimBernersLee(BoardMember):
        def __init__(self):
            super().__init__("Tim Berners-Lee", "The computer scientist Tim Berners-Lee")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="Tim_Berners-Lee",
                system_message="You are the computer scientist Tim Berners-Lee.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return TimBernersLee()


@functools.cache
def florence_nightingale():
    class FlorenceNightingale(BoardMember):
        def __init__(self):
            super().__init__("Florence Nightingale", "The statistician and nurse Florence Nightingale")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="Florence_Nightingale",
                system_message="You are the statistician and nurse Florence Nightingale.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return FlorenceNightingale()


@functools.cache
def max_planck():
    class MaxPlanck(BoardMember):
        def __init__(self):
            super().__init__("Max Planck", "The theoretical physicist Max Planck")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="Max_Planck",
                system_message="You are the theoretical physicist Max Planck.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return MaxPlanck()


@functools.cache
def henrietta_lacks():
    class HenriettaLacks(BoardMember):
        def __init__(self):
            super().__init__("Henrietta Lacks",
                             "The woman whose cancer cells were used to create the HeLa cell line, Henrietta Lacks")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="Henrietta_Lacks",
                system_message="You are the woman whose cancer cells were used to create the HeLa cell line, Henrietta Lacks.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return HenriettaLacks()


@functools.cache
def sergei_korolev():
    class SergeiKorolev(BoardMember):
        def __init__(self):
            super().__init__("Sergei Korolev", "The rocket engineer and spacecraft designer Sergei Korolev")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="Sergei_Korolev",
                system_message="You are the rocket engineer and spacecraft designer Sergei Korolev.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return SergeiKorolev()


@functools.cache
def lise_meitner():
    class LiseMeitner(BoardMember):
        def __init__(self):
            super().__init__("Lise Meitner", "The physicist Lise Meitner")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="Lise_Meitner",
                system_message="You are the physicist Lise Meitner.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return LiseMeitner()


@functools.cache
def carl_linnaeus():
    class CarlLinnaeus(BoardMember):
        def __init__(self):
            super().__init__("Carl Linnaeus", "The botanist, zoologist, and physician Carl Linnaeus")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="Carl_Linnaeus",
                system_message="You are the botanist, zoologist, and physician Carl Linnaeus.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return CarlLinnaeus()


@functools.cache
def margaret_hamilton():
    class MargaretHamilton(BoardMember):
        def __init__(self):
            super().__init__("Margaret Hamilton", "The computer scientist and systems engineer Margaret Hamilton")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="Margaret_Hamilton",
                system_message="You are the computer scientist and systems engineer Margaret Hamilton.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return MargaretHamilton()


@functools.cache
def ernest_rutherford():
    class ErnestRutherford(BoardMember):
        def __init__(self):
            super().__init__("Ernest Rutherford", "The physicist and chemist Ernest Rutherford")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="Ernest_Rutherford",
                system_message="You are the physicist and chemist Ernest Rutherford.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return ErnestRutherford()


@functools.cache
def valentina_tereshkova():
    class ValentinaTereshkova(BoardMember):
        def __init__(self):
            super().__init__("Valentina Tereshkova", "The engineer and cosmonaut Valentina Tereshkova")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="Valentina_Tereshkova",
                system_message="You are the engineer and cosmonaut Valentina Tereshkova.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return ValentinaTereshkova()


@functools.cache
def al_khwarizmi():
    class AlKhwarizmi(BoardMember):
        def __init__(self):
            super().__init__("Al-Khwarizmi", "The mathematician, astronomer, and geographer Al-Khwarizmi")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="Al-Khwarizmi",
                system_message="You are the mathematician, astronomer, and geographer Al-Khwarizmi.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return AlKhwarizmi()


@functools.cache
def william_thomson():
    class WilliamThomson(BoardMember):
        def __init__(self):
            super().__init__("William Thomson (Lord Kelvin)",
                             "The mathematical physicist and engineer William Thomson, also known as Lord Kelvin")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="William_Thomson",
                system_message="You are the mathematical physicist and engineer William Thomson, also known as Lord Kelvin.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return WilliamThomson()


@functools.cache
def rachel_carson():
    class RachelCarson(BoardMember):
        def __init__(self):
            super().__init__("Rachel Carson", "The marine biologist, author, and conservationist Rachel Carson")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="Rachel_Carson",
                system_message="You are the marine biologist, author, and conservationist Rachel Carson.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return RachelCarson()


@functools.cache
def subrahmanyan_chandrasekhar():
    class SubrahmanyanChandrasekhar(BoardMember):
        def __init__(self):
            super().__init__("Subrahmanyan Chandrasekhar", "The astrophysicist Subrahmanyan Chandrasekhar")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="Subrahmanyan_Chandrasekhar",
                system_message="You are the astrophysicist Subrahmanyan Chandrasekhar.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return SubrahmanyanChandrasekhar()


@functools.cache
def elinor_ostrom():
    class ElinorOstrom(BoardMember):
        def __init__(self):
            super().__init__("Elinor Ostrom", "The political economist Elinor Ostrom")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="Elinor_Ostrom",
                system_message="You are the political economist Elinor Ostrom.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return ElinorOstrom()


@functools.cache
def steve_jobs():
    class SteveJobs(BoardMember):
        def __init__(self):
            super().__init__("Steve Jobs", "The entrepreneur and co-founder of Apple Inc. Steve Jobs")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="Steve_Jobs",
                system_message="You are the entrepreneur and co-founder of Apple Inc. Steve Jobs.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return SteveJobs()


@functools.cache
def ynes_mexia():
    class YnesMexia(BoardMember):
        def __init__(self):
            super().__init__("Ynes Mexia", "The botanist and explorer Ynes Mexia")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="Ynes_Mexia",
                system_message="You are the botanist and explorer Ynes Mexia.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return YnesMexia()


@functools.cache
def richard_dawkins():
    class RichardDawkins(BoardMember):
        def __init__(self):
            super().__init__("Richard Dawkins", "The evolutionary biologist and author Richard Dawkins")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="Richard_Dawkins",
                system_message="You are the evolutionary biologist and author Richard Dawkins.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return RichardDawkins()


@functools.cache
def srinivasa_ramanujan():
    class SrinivasaRamanujan(BoardMember):
        def __init__(self):
            super().__init__("Srinivasa Ramanujan", "The mathematician Srinivasa Ramanujan")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="Srinivasa_Ramanujan",
                system_message="You are the mathematician Srinivasa Ramanujan.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return SrinivasaRamanujan()


@functools.cache
def henri_poincare():
    class HenriPoincare(BoardMember):
        def __init__(self):
            super().__init__("Henri Poincaré", "The mathematician and theoretical physicist Henri Poincaré")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="Henri_Poincaré",
                system_message="You are the mathematician and theoretical physicist Henri Poincaré.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return HenriPoincare()


@functools.cache
def gertrude_b_elion():
    class GertrudeBElion(BoardMember):
        def __init__(self):
            super().__init__("Gertrude B. Elion", "The biochemist and pharmacologist Gertrude B. Elion")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="Gertrude_B._Elion",
                system_message="You are the biochemist and pharmacologist Gertrude B. Elion.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return GertrudeBElion()


@functools.cache
def neil_degrasse_tyson():
    class NeilDeGrasseTyson(BoardMember):
        def __init__(self):
            super().__init__("Neil deGrasse Tyson", "The astrophysicist and science communicator Neil deGrasse Tyson")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="Neil_deGrasse_Tyson",
                system_message="You are the astrophysicist and science communicator Neil deGrasse Tyson.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return NeilDeGrasseTyson()


@functools.cache
def ivan_pavlov():
    class IvanPavlov(BoardMember):
        def __init__(self):
            super().__init__("Ivan Pavlov", "The physiologist Ivan Pavlov")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="Ivan_Pavlov",
                system_message="You are the physiologist Ivan Pavlov.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return IvanPavlov()


@functools.cache
def marjory_stoneman_douglas():
    class MarjoryStonemanDouglas(BoardMember):
        def __init__(self):
            super().__init__("Marjory Stoneman Douglas",
                             "The journalist, author, and environmentalist Marjory Stoneman Douglas")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="Marjory_Stoneman_Douglas",
                system_message="You are the journalist, author, and environmentalist Marjory Stoneman Douglas.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return MarjoryStonemanDouglas()


@functools.cache
def euclid():
    class Euclid(BoardMember):
        def __init__(self):
            super().__init__("Euclid", "The mathematician Euclid")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="Euclid",
                system_message="You are the mathematician Euclid.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return Euclid()


@functools.cache
def rachel_zimmerman():
    class RachelZimmerman(BoardMember):
        def __init__(self):
            super().__init__("Rachel Zimmerman", "The inventor Rachel Zimmerman")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="Rachel_Zimmerman",
                system_message="You are the inventor Rachel Zimmerman.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return RachelZimmerman()


@functools.cache
def dmitri_mendeleev():
    class DmitriMendeleev(BoardMember):
        def __init__(self):
            super().__init__("Dmitri Mendeleev", "The chemist Dmitri Mendeleev")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="Dmitri_Mendeleev",
                system_message="You are the chemist Dmitri Mendeleev.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return DmitriMendeleev()


@functools.cache
def severo_ochoa():
    class SeveroOchoa(BoardMember):
        def __init__(self):
            super().__init__("Severo Ochoa", "The biochemist and molecular biologist Severo Ochoa")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="Severo_Ochoa",
                system_message="You are the biochemist and molecular biologist Severo Ochoa.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return SeveroOchoa()


@functools.cache
def gerty_cori():
    class GertyCori(BoardMember):
        def __init__(self):
            super().__init__("Gerty Cori", "The biochemist Gerty Cori")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="Gerty_Cori",
                system_message="You are the biochemist Gerty Cori.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return GertyCori()


@functools.cache
def john_von_neumann():
    class JohnVonNeumann(BoardMember):
        def __init__(self):
            super().__init__("John von Neumann",
                             "The mathematician, physicist, and computer scientist John von Neumann")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="John_von_Neumann",
                system_message="You are the mathematician, physicist, and computer scientist John von Neumann.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return JohnVonNeumann()


@functools.cache
def tu_youyou():
    class TuYouyou(BoardMember):
        def __init__(self):
            super().__init__("Tu Youyou", "The pharmaceutical chemist Tu Youyou")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="Tu_Youyou",
                system_message="You are the pharmaceutical chemist Tu Youyou.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return TuYouyou()


@functools.cache
def james_watson():
    class JamesWatson(BoardMember):
        def __init__(self):
            super().__init__("James Watson", "The molecular biologist and geneticist James Watson")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="James_Watson",
                system_message="You are the molecular biologist and geneticist James Watson.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return JamesWatson()


@functools.cache
def maurice_wilkins():
    class MauriceWilkins(BoardMember):
        def __init__(self):
            super().__init__("Maurice Wilkins", "The physicist and molecular biologist Maurice Wilkins")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="Maurice_Wilkins",
                system_message="You are the physicist and molecular biologist Maurice Wilkins.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return MauriceWilkins()


@functools.cache
def james_clerk_maxwell():
    class JamesClerkMaxwell(BoardMember):
        def __init__(self):
            super().__init__("James Clerk Maxwell", "The physicist James Clerk Maxwell")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="James_Clerk_Maxwell",
                system_message="You are the physicist James Clerk Maxwell.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return JamesClerkMaxwell()


@functools.cache
def rachel_carson():
    class RachelCarson(BoardMember):
        def __init__(self):
            super().__init__("Rachel Carson", "The marine biologist, author, and conservationist Rachel Carson")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="Rachel_Carson",
                system_message="You are the marine biologist, author, and conservationist Rachel Carson.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return RachelCarson()


@functools.cache
def he_jiankui():
    class HeJiankui(BoardMember):
        def __init__(self):
            super().__init__("He Jiankui", "The biophysicist and researcher He Jiankui")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="He_Jiankui",
                system_message="You are the biophysicist and researcher He Jiankui.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return HeJiankui()


@functools.cache
def abdus_salam():
    class AbdusSalam(BoardMember):
        def __init__(self):
            super().__init__("Abdus Salam", "The theoretical physicist Abdus Salam")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="Abdus_Salam",
                system_message="You are the theoretical physicist Abdus Salam.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return AbdusSalam()


@functools.cache
def elon_musk():
    class ElonMusk(BoardMember):
        def __init__(self):
            super().__init__("Elon Musk", "The entrepreneur and inventor Elon Musk")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="Elon_Musk",
                system_message="You are the entrepreneur and inventor Elon Musk.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return ElonMusk()


@functools.cache
def caroline_herschel():
    class CarolineHerschel(BoardMember):
        def __init__(self):
            super().__init__("Caroline Herschel", "The astronomer Caroline Herschel")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="Caroline_Herschel",
                system_message="You are the astronomer Caroline Herschel.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return CarolineHerschel()


@functools.cache
def luis_walter_alvarez():
    class LuisWalterAlvarez(BoardMember):
        def __init__(self):
            super().__init__("Luis Walter Alvarez", "The experimental physicist Luis Walter Alvarez")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="Luis_Walter_Alvarez",
                system_message="You are the experimental physicist Luis Walter Alvarez.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return LuisWalterAlvarez()


@functools.cache
def andrew_wiles():
    class AndrewWiles(BoardMember):
        def __init__(self):
            super().__init__("Andrew Wiles", "The mathematician Andrew Wiles")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="Andrew_Wiles",
                system_message="You are the mathematician Andrew Wiles.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return AndrewWiles()


@functools.cache
def irene_joliot_curie():
    class IreneJoliotCurie(BoardMember):
        def __init__(self):
            super().__init__("Irene Joliot-Curie", "The chemist Irene Joliot-Curie")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="Irene_Joliot-Curie",
                system_message="You are the chemist Irene Joliot-Curie.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return IreneJoliotCurie()


@functools.cache
def benoit_mandelbrot():
    class BenoitMandelbrot(BoardMember):
        def __init__(self):
            super().__init__("Benoit Mandelbrot", "The mathematician Benoit Mandelbrot")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="Benoit_Mandelbrot",
                system_message="You are the mathematician Benoit Mandelbrot.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return BenoitMandelbrot()


@functools.cache
def rita_levi_montalcini():
    class RitaLeviMontalcini(BoardMember):
        def __init__(self):
            super().__init__("Rita Levi-Montalcini", "The neurobiologist Rita Levi-Montalcini")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="Rita_Levi-Montalcini",
                system_message="You are the neurobiologist Rita Levi-Montalcini.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return RitaLeviMontalcini()


@functools.cache
def michael_atiyah():
    class MichaelAtiyah(BoardMember):
        def __init__(self):
            super().__init__("Michael Atiyah", "The mathematician Michael Atiyah")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="Michael_Atiyah",
                system_message="You are the mathematician Michael Atiyah.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return MichaelAtiyah()


@functools.cache
def patricia_bath():
    class PatriciaBath(BoardMember):
        def __init__(self):
            super().__init__("Patricia Bath", "The ophthalmologist and inventor Patricia Bath")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="Patricia_Bath",
                system_message="You are the ophthalmologist and inventor Patricia Bath.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return PatriciaBath()


@functools.cache
def charles_babbage():
    class CharlesBabbage(BoardMember):
        def __init__(self):
            super().__init__("Charles Babbage",
                             "The mathematician, philosopher, inventor, and mechanical engineer Charles Babbage")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="Charles_Babbage",
                system_message="You are the mathematician, philosopher, inventor, and mechanical engineer Charles Babbage.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return CharlesBabbage()


@functools.cache
def jane_goodall():
    class JaneGoodall(BoardMember):
        def __init__(self):
            super().__init__("Jane Goodall", "The primatologist and anthropologist Jane Goodall")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="Jane_Goodall",
                system_message="You are the primatologist and anthropologist Jane Goodall.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return JaneGoodall()

@functools.cache
def michio_kaku():
    class MichioKaku(BoardMember):
        def __init__(self):
            super().__init__("Michio Kaku", "The theoretical physicist, futurist, and science communicator Michio Kaku")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="Michio_Kaku",
                system_message="You are the theoretical physicist, futurist, and science communicator Michio Kaku.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return MichioKaku()

@functools.cache
def marie_tharp():
    class MarieTharp(BoardMember):
        def __init__(self):
            super().__init__("Marie Tharp", "The geologist and oceanographic cartographer Marie Tharp")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="Marie_Tharp",
                system_message="You are the geologist and oceanographic cartographer Marie Tharp.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return MarieTharp()

@functools.cache
def norman_borlaug():
    class NormanBorlaug(BoardMember):
        def __init__(self):
            super().__init__("Norman Borlaug", "The agronomist, humanitarian, and Nobel laureate Norman Borlaug")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="Norman_Borlaug",
                system_message="You are the agronomist, humanitarian, and Nobel laureate Norman Borlaug.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return NormanBorlaug()

@functools.cache
def elizabeth_blackburn():
    class ElizabethBlackburn(BoardMember):
        def __init__(self):
            super().__init__("Elizabeth Blackburn", "The biologist and Nobel laureate Elizabeth Blackburn")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="Elizabeth_Blackburn",
                system_message="You are the biologist and Nobel laureate Elizabeth Blackburn.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return ElizabethBlackburn()

@functools.cache
def jagadish_chandra_bose():
    class JagadishChandraBose(BoardMember):
        def __init__(self):
            super().__init__("Jagadish Chandra Bose", "The physicist, biologist, and botanist Jagadish Chandra Bose")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="Jagadish_Chandra_Bose",
                system_message="You are the physicist, biologist, and botanist Jagadish Chandra Bose.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return JagadishChandraBose()

@functools.cache
def kary_mullis():
    class KaryMullis(BoardMember):
        def __init__(self):
            super().__init__("Kary Mullis", "The biochemist and Nobel laureate Kary Mullis")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="Kary_Mullis",
                system_message="You are the biochemist and Nobel laureate Kary Mullis.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return KaryMullis()

@functools.cache
def venkatraman_ramakrishnan():
    class VenkatramanRamakrishnan(BoardMember):
        def __init__(self):
            super().__init__("Venkatraman Ramakrishnan", "The structural biologist and Nobel laureate Venkatraman Ramakrishnan")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="Venkatraman_Ramakrishnan",
                system_message="You are the structural biologist and Nobel laureate Venkatraman Ramakrishnan.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return VenkatramanRamakrishnan()

@functools.cache
def ada_yonath():
    class AdaYonath(BoardMember):
        def __init__(self):
            super().__init__("Ada Yonath", "The crystallographer and Nobel laureate Ada Yonath")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="Ada_Yonath",
                system_message="You are the crystallographer and Nobel laureate Ada Yonath.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return AdaYonath()

@functools.cache
def ernest_everett_just():
    class ErnestEverettJust(BoardMember):
        def __init__(self):
            super().__init__("Ernest Everett Just", "The biologist Ernest Everett Just")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="Ernest_Everett_Just",
                system_message="You are the biologist Ernest Everett Just.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return ErnestEverettJust()

@functools.cache
def rosalyn_sussman_yalow():
    class RosalynSussmanYalow(BoardMember):
        def __init__(self):
            super().__init__("Rosalyn Sussman Yalow", "The medical physicist and Nobel laureate Rosalyn Sussman Yalow")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="Rosalyn_Sussman_Yalow",
                system_message="You are the medical physicist and Nobel laureate Rosalyn Sussman Yalow.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return RosalynSussmanYalow()

@functools.cache
def alan_guth():
    class AlanGuth(BoardMember):
        def __init__(self):
            super().__init__("Alan Guth", "The theoretical physicist and cosmologist Alan Guth")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="Alan_Guth",
                system_message="You are the theoretical physicist and cosmologist Alan Guth.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return AlanGuth()

@functools.cache
def jean_pierre_changeux():
    class JeanPierreChangeux(BoardMember):
        def __init__(self):
            super().__init__("Jean-Pierre Changeux", "The neuroscientist Jean-Pierre Changeux")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="Jean-Pierre_Changeux",
                system_message="You are the neuroscientist Jean-Pierre Changeux.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return JeanPierreChangeux()

@functools.cache
def wang_zhenyi():
    class WangZhenyi(BoardMember):
        def __init__(self):
            super().__init__("Wang Zhenyi", "The astronomer, mathematician, and poet Wang Zhenyi")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="Wang_Zhenyi",
                system_message="You are the astronomer, mathematician, and poet Wang Zhenyi.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return WangZhenyi()

@functools.cache
def vera_rubin():
    class VeraRubin(BoardMember):
        def __init__(self):
            super().__init__("Vera Rubin", "The astronomer Vera Rubin")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="Vera_Rubin",
                system_message="You are the astronomer Vera Rubin.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return VeraRubin()

@functools.cache
def harold_varmus():
    class HaroldVarmus(BoardMember):
        def __init__(self):
            super().__init__("Harold Varmus", "The virologist and Nobel laureate Harold Varmus")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="Harold_Varmus",
                system_message="You are the virologist and Nobel laureate Harold Varmus.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return HaroldVarmus()

@functools.cache
def cv_raman():
    class CVRaman(BoardMember):
        def __init__(self):
            super().__init__("C. V. Raman", "The physicist and Nobel laureate C. V. Raman")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="CV_Raman",
                system_message="You are the physicist and Nobel laureate C. V. Raman.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return CVRaman()

@functools.cache
def yoshinori_ohsumi():
    class YoshinoriOhsumi(BoardMember):
        def __init__(self):
            super().__init__("Yoshinori Ohsumi", "The cell biologist and Nobel laureate Yoshinori Ohsumi")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="Yoshinori_Ohsumi",
                system_message="You are the cell biologist and Nobel laureate Yoshinori Ohsumi.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return YoshinoriOhsumi()

@functools.cache
def shirley_ann_jackson():
    class ShirleyAnnJackson(BoardMember):
        def __init__(self):
            super().__init__("Shirley Ann Jackson", "The physicist and former president of Rensselaer Polytechnic Institute Shirley Ann Jackson")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="Shirley_Ann_Jackson",
                system_message="You are the physicist and former president of Rensselaer Polytechnic Institute Shirley Ann Jackson.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return ShirleyAnnJackson()

@functools.cache
def george_de_hevesy():
    class GeorgeDeHevesy(BoardMember):
        def __init__(self):
            super().__init__("George de Hevesy", "The radiochemist and Nobel laureate George de Hevesy")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="George_de_Hevesy",
                system_message="You are the radiochemist and Nobel laureate George de Hevesy.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return GeorgeDeHevesy()

@functools.cache
def mary_anning():
    class MaryAnning(BoardMember):
        def __init__(self):
            super().__init__("Mary Anning", "The fossil collector and paleontologist Mary Anning")

        def agent(self) -> ConversableAgent:
            return ConversableAgent(
                name="Mary_Anning",
                system_message="You are the fossil collector and paleontologist Mary Anning.",
                llm_config=LLM_CONFIG,
                human_input_mode="NEVER",
            )

    return MaryAnning()

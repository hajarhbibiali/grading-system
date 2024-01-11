from fastapi import FastAPI
import strawberry
from strawberry.asgi import GraphQL
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from static.models.all_models import predict

# https://www.tutorialspoint.com/fastapi/fastapi_using_graphql.htm tuto


@strawberry.type
class Question:
    question_id: int
    question: str


@strawberry.type
class Answer:
    question_id: int
    answer: str


@strawberry.type
class Grade:
    question_id: int
    answer: str
    grade: int


@strawberry.type
class Mutation:
    @strawberry.mutation
    def recover_answer(self, question_id: int, answer: str) -> Grade:
        grade = predict( answer)
        new_answer = Grade(question_id=question_id, answer=answer, grade=grade)
        return new_answer


@strawberry.type
class Query:
    @strawberry.field
    def questions(self) -> List[Question]:
        return [
            Question(
                question_id=1,
                question="من هو خاتم الأنبياء والمرسلين؟ ",
            ),
            Question(
                question_id=2,
                question="كم استمرت الدعوة السرية؟"
            ),
            Question(question_id=3,
                      question="ما هي السور التي بدأت بالحمد ؟ "),
            Question(
                question_id=4, question="ما هو اسم والدة نبي الله عيسى عليه السلام؟"
            ),
            Question(question_id=5, question="من هي أول من دخل في الإسلام من النساء؟"),
            Question(
                question_id=6, question="ما هي السورة التي لا تبتدأ بالبسملة ؟"
            ),
            Question(
                question_id=7,
                question="ما هو اسم مرضعة الرسول صلى الله عليه وسلم؟",
            ),
            Question(
                question_id=8, question=" من هو النبي الذي التقمه الحوت؟"
            ),
            Question(
                question_id=9,
                question="ما هي السورة التي تحدثت عن تقسيم الغنائم؟",
            ),
            Question(question_id=10, question="ما هي أقصر سورة في القرآن الكريم ؟"),
        ]

    @strawberry.field
    def corr_answers(self) -> List[Answer]:
        return [
            Answer(
                question_id=1,
                answer="محمد صلى الله عليه وسلم",
            ),
            Answer(
                question_id=2,
                answer="استمرت الدعوة السرية ثلاث سنوات"
            ),
            Answer(
                question_id=3,
                answer="السور التي تفتتح بالحمد هي: الفاتحة، الأنعام، الكهف، سبأ، وفاطر",
            ),
            Answer(
                question_id=4,
                answer="اسم والدة نبي الله عيسى عليه السلام هو السيدة مريم عليها السلام",
            ),
            Answer(
                question_id=5,
                answer=" خديجة بنت خويلد، رضي الله عنها، هي أول امرأة أسلمت على رسول الله صلى الله عليه وسلم",
            ),
            Answer(
                question_id=6,
                answer="سورة التوبة" ,
            ),
            Answer(
                question_id=7,
                answer="حليمة السعدية رضي الله",
            ),
            Answer(
                question_id=8,
                answer="النبي الذي  التقمه  الحوت هو النبي يونس عليه السلام",
            ),
            Answer(
                question_id=9,
                answer=" سورة الأنفال ",
            ),
            Answer(
                
                question_id=10,
                answer="سورة الكوثر هي أصغر سورة في القرآن,",
            ),
        ]


schema = strawberry.Schema(query=Query, mutation=Mutation)

graphql_app = GraphQL(schema)
app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_route("/", graphql_app)
app.add_websocket_route("/", graphql_app)

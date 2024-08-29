import google.generativeai as genai
import os


def get_car_ai_description(model, brand, year):

    prompt = "Me mostre uma descrição de venda para o carro {} {} {} em até 250 caractéres. Fale cooisas específicas deste carro"

    
    gem_api_key = os.getenv('GOOGLE_API_KEY')
    genai.configure(api_key=gem_api_key)    


    prompt = prompt.format(brand, model, year)
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(prompt)

    return response.text
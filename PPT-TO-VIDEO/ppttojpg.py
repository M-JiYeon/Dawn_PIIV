import os
import sys
import win32com
import win32com.client

ppSaveAsJPG = 17

def ppt_to_jpg(ppt_file_name,output_dir_name):
	'''PPT를 JPG로 저장하기
		arguments :
		ppt_file_name : 변환할 ppt 파일,
		output_dir_name: JPG 문장으로 변환파일의 디렉터리'''
	# ppt 시작
	ppt_app = win32com.client.Dispatch('PowerPoint.Application')
	# 0으로 설정하면 백그라운드가 실행됩니다. 보이지 않고, 1이 표시됩니다.
	ppt_app.Visible = 1
	# ppt 열기
	ppt = ppt_app.Presentations.Open(ppt_file_name)
	# 다른 이름 저장
	ppt.SaveAs(output_dir_name, ppSaveAsJPG)
	# 출력
	ppt_app.Quit()

if __name__ == '__main__':
	current_dir = os.sys.path[0]
	dir_list = os.listdir(current_dir)
	# 현재 파일에 있는 모든 ppt 파일 ,eg: ppt_name.ppt
	ppt_file_names = (fns for fns in dir_list if fns.endswith(('.ppt','.pptx')))
	# 현재 파일에 있는 모든 ppt 이름,eg: ppt_name
	ppt_names = (os.path.splitext(fns)[0] for fns in dir_list if fns.endswith(('.ppt','.pptx')))
	# ppt_names = (fns.split('.')[0] for fns in dir_list if fns.endswith(('.ppt','.pptx')))
	for ppt_file_name,ppt_name in zip(ppt_file_names,ppt_names):
		# PPT의 전체 경로 파일 이름，eg: F:\\test\\ppt_name.ppt
		ppt_file_name = os.path.join(current_dir,ppt_file_name)
		# PPT와 같은 이름의 파일을 새로 만들어 전체 경로를 가져와야 합니다,eg:  F:\\test\\ppt_name
		ppt_dir_path = os.path.join(current_dir,ppt_name)
		os.mkdir(ppt_dir_path)
		# print ppt_file_name, ppt_dir_path
		ppt_to_jpg(ppt_file_name,ppt_dir_path)
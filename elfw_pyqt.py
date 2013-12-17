
import re,os,shutil,sys,time
from PyQt4 import QtGui, QtCore

def search_location (search_dir,para1,para2,para3):
	path=search_dir
	match_string=r'.*'+para1+r'.*'+para2+r'.*'+para3
	for file1 in os.listdir(path):
		pattern=re.compile(match_string)
		match=pattern.match(file1)
		if match:
			build=match.group()
	return build    
	   
def search_list (search_list,para1,para2,para3):
	match_string=r'.*'+para1+r'.*'+para2+r'.*'+para3
	for file1 in search_list:
		pattern=re.compile(match_string)
		match=pattern.match(file1)
		if match:
			build=match.group()
	return build

def get_board_type (configID):
	type1=''.join(configID[0:2])
	if type1 == '25':
		board_type='2582'
	elif type1 == '29':
		board_type='2281'    
	elif type1 == '27':
		board_type='2281'
	elif type1 == '22':
		board_type='2281' 
	elif type1 == '28':
		board_type='2281'
	elif type1 == '2241':
		board_type='2281'
	elif type1 == '31':
		board_type='2281'
	elif type1 == '33':
		board_type='2281'      
	return board_type
					
def get_cli_no(location,board_config):
	targetdir=location+'\\cfg_customer\\db\\PPRO_tbl_master_config.csv'
	if os.path.exists (targetdir):
		f=open(targetdir)
		for line in f:
			pattern=re.compile(r'.*'+board_config+'.*,PP-C(\w{5}),PP-R(\w{5})')
			match=pattern.match(line)
			if match:
				return match.group(1)
		f.close()
	else:
		print "no found mastertable"

def get_cli_nobylocal(location,board_config):
	if os.path.exists (location):
		f=open(location)
		for line in f:
			pattern=re.compile(r'.*'+board_config+'.*,PP-C(\w{5}),PP-R(\w{5})')
			match=pattern.match(line)
			if match:
				return match.group(1)
		f.close()
	else:
		print "no found mastertable"
			
def getbuildno (search_dir,para1):
	list1=[]
	match_string=r'.*'+para1+r'.*'
	for file1 in os.listdir(search_dir):
		pattern=re.compile(match_string)
		match=pattern.match(file1)
		if match:
			h=match.group()
			match_string1=r'(.*)(\d{6})'
			pattern1=re.compile(match_string1)
			match1=pattern1.match(h)
			if match1:
				list1.append(match1.group(2))
	list1.sort()        
	return list1[-1]

def getbuildnobylist (search_list,para1):
	list1=[]
	match_string=r'.*'+para1+r'.*'
	for file1 in search_list:
		pattern=re.compile(match_string)
		match=pattern.match(file1)
		if match:
			h=match.group()
			match_string1=r'(.*)(\d{6})'
			pattern1=re.compile(match_string1)
			match1=pattern1.match(h)
			if match1:
				list1.append(match1.group(2))
	list1.sort()        
	return list1[-1]

def getbuildlabel(string):
	newstring=''
	for c in string[0:3]:
		b=c.upper()+'_'
		newstring=newstring+b
	if len(string) ==3 :
		newstring +="Release"
	else:
		if string[-1] =="c":
			newstring +="CLI"
		else:
			raise Exception(" string not equal 3")
	return newstring

def getlist(samba_location):
	list_fw=[]
	if os.path.isfile(samba_location):
		for files in open(samba_location):
			list_fw.append(files)
	else:
		for files in os.listdir(samba_location):
			list_fw.append(files)
	return list_fw

class Window( QtGui.QWidget ):
	def __init__( self ):

		super( Window, self ).__init__()

		self.setWindowTitle( "hello" )
		self.resize( 500, 500 )

		self.default_local_smart_download='Z:\\sd\\builds'
		self.default_elf_location='Z:'

		self.master_table_file='PPRO_tbl_master_config.csv'
		self.source_master_table_dir=self.default_local_smart_download+'\\'+'mastertable'+'\\'+'cfg_customer'+'\\'+'db'

		self.fw_location=r'\\samba-fcd2'+'\\'+'fwbuilds'

		
		if os.path.isfile('fw_list.dat') is not True :
			fw_file=open('fw_list.dat', 'w')
			for str_list_fw in getlist(self.fw_location):
				fw_file.write(str_list_fw +'\n')
			fw_file.close()
		self.list_fw = getlist('fw_list.dat')

		self.sign1 = QtGui.QLabel(self)
		self.sign1.move(10, 30)
		self.sign1.setText("Input build lable or build no below:")
		self.sign3 = QtGui.QLabel(self)
		self.sign3.move(300, 30)
		self.sign3.setText("dump stamp to: %s" %self.default_local_smart_download)
		self.build = QtGui.QLineEdit(self)
		self.build.move(10, 50)

		self.sign2 = QtGui.QLabel(self)
		self.sign2.move(10, 80)
		self.sign2.setText("Input configID below:" )
		self.sign4 = QtGui.QLabel(self)
		self.sign4.move(300, 80)
		self.sign4.setText("dump elf to: %s" %self.default_elf_location)
		self.config = QtGui.QLineEdit(self)
		self.config.move(10, 100) 
		
		# self.lb_stamp1 = QtGui.QLabel(self)
		# self.lb_stamp1.move(10, 150)
		# self.lb_stamp1.setText("stamp_fw")
		# self.lb_stamp1.adjustSize()  

		# self.lb_stamp2 = QtGui.QLabel(self)
		# self.lb_stamp2.move(10, 180)
		# self.lb_stamp2.setText("stamp_mf")
		# self.lb_stamp2.adjustSize()  
		#self.lb_stamp.setGeometry(QtCore.QRect(20,80,201,22))

		# self.lbl_elf = QtGui.QLabel(self)
		# self.lbl_elf.move(10, 210)
		# self.lbl_elf.setText("fw_elf")
		# self.lbl_elf.adjustSize()

		# self.lbl_vic = QtGui.QLabel(self)
		# self.lbl_vic.move(10, 240)
		# self.lbl_vic.setText("fw_vic")
		# self.lbl_vic.adjustSize()

		# self.lbl_mf = QtGui.QLabel(self)
		# self.lbl_mf.move(10, 270)
		# self.lbl_mf.setText("mf_vic")
		# self.lbl_mf.adjustSize()

		self.test_message = QtGui.QTextEdit(self)
		self.test_message.move(10, 210)
		# self.qbtn_search = QtGui.QPushButton('search Elf', self)
		# self.qbtn_search.move(50, 430) 
		# self.connect( self.qbtn_search, QtCore.SIGNAL( 'clicked()' ), self.onSearchElf )

		# self.qbtn_search2 = QtGui.QPushButton('search Stamp', self)
		# self.qbtn_search2.move(50, 410) 
		# self.connect( self.qbtn_search2, QtCore.SIGNAL( 'clicked()' ), self.onSearchStamp )

		self.qbtn_dump1 = QtGui.QPushButton('dump stamp image', self)
		self.qbtn_dump1.move(200, 430)  
		self.connect( self.qbtn_dump1, QtCore.SIGNAL( 'clicked()' ), self.dumpStamp )

		self.qbtn_dump2 = QtGui.QPushButton('dump elf', self)
		self.qbtn_dump2.move(400, 430)
		self.connect( self.qbtn_dump2, QtCore.SIGNAL( 'clicked()' ), self.dumpElf )

		self.status = QtGui.QLabel(self)
		self.status.move(10, 480)
		self.status.setText("Ready")

		#build= str(self.build.text())
		#self.build.setText(search_list(self.list_fw, getbuildnobylist(self.list_fw, getbuildlabel(build)), '', ''))

	def onSearchElf(self):
		build= str(self.build.text())
		configid=str(self.config.text())

		if len(build) == 6:
			self.build_location=search_list(self.list_fw, build, '', '')#search_location(self.fw_location, build, '', '')
		else :
			self.build_location=search_list(self.list_fw, getbuildnobylist(self.list_fw, getbuildlabel(build)), '', '')#search_location(self.fw_location, getbuildno(self.fw_location, getbuildlabel(build)), '', '')

		board_type = get_board_type(configid)

		cli_no = get_cli_nobylocal(self.source_master_table_dir+'\\'+self.master_table_file,configid)

		board_location = 'SF-'+board_type+'_Board'
		self.fw_elf= search_location(self.fw_location+'\\'+self.build_location+'\\'+board_location,'fw',cli_no,'elf')  

		full_board_location=self.fw_location+'\\'+self.build_location+'\\'+board_location+'\\'

		self.lbl_elf.setText(full_board_location+self.fw_elf)
		self.lbl_elf.adjustSize()

	def onSearchStamp(self,configid):
		build= str(self.build.text())

		if len(build) == 6:
			self.build_location=search_list(self.list_fw, build, '', '')
		else :
			self.build_location=search_list(self.list_fw, getbuildnobylist(self.list_fw, getbuildlabel(build)), '', '')

		board_type = get_board_type(configid)

		cli_no = get_cli_nobylocal(self.source_master_table_dir+'\\'+self.master_table_file, configid)

		board_location = 'SF-'+board_type+'_Board'

		self.full_stamp_location=self.fw_location+'\\'+self.build_location+'\\'+'stamped_images'

		self.stamp_list =getlist(self.full_stamp_location)

		self.vic_file = search_list(self.stamp_list ,'C'+configid,'fw','vic')
		self.mf_file  = search_list(self.stamp_list ,'C'+configid,'mf','vic')

	def dumpStamp(self):
		configid=str(self.config.text())
		for config in configid.split(';'):
			self.onSearchStamp(config)

			if not os.path.exists(self.default_local_smart_download+'\\'+self.build_location+'\\'+'stamped_images'+'\\') :
				os.makedirs(self.default_local_smart_download+'\\'+self.build_location+'\\'+'stamped_images'+'\\')

			target_master_table_dir=self.default_local_smart_download+'\\'+self.build_location+'\\'+'cfg_customer'+'\\'+'db'
			if not os.path.exists(target_master_table_dir):
				os.makedirs(target_master_table_dir)
			if os.path.isfile(target_master_table_dir+'\\'+self.master_table_file) is not True:
				shutil.copyfile(self.source_master_table_dir+'\\'+self.master_table_file,\
				target_master_table_dir+'\\'+self.master_table_file)

			try:
				local_stamp_location = self.default_local_smart_download+'\\'+self.build_location+'\\'+'stamped_images'

				source1=self.full_stamp_location+'\\'+self.vic_file
				target1=local_stamp_location +'\\'+self.vic_file

				if os.path.isfile(target1) is not True:
					shutil.copyfile(source1,target1)
					self.test_message.append(" %s VIC file dumped" %config)
				else:
					self.test_message.append(" %s VIC file already exists" %config)

				source2=self.full_stamp_location+'\\'+self.mf_file
				target2=local_stamp_location+'\\'+self.mf_file

				if os.path.isfile(target2) is not True:
					shutil.copyfile(source2,target2)
					self.test_message.append(" %s MF file dumped" %config)
				else:
					self.test_message.append("%s MF file already exists" %config)

			except:
				self.test_message.append("Error occured while VIC/MF dumping")

	def dumpElf(self):
		self.onSearchElf()
		try:
			shutil.copyfile(str(self.lbl_elf.text()), self.default_elf_location+'\\'+self.fw_elf)
			self.test_message.append("Succeed to copy elf ")
		except:
			self.test_message.append("Error occured while elf dumping")

app = QtGui.QApplication( sys.argv )
win = Window()
win.show()
app.exec_()
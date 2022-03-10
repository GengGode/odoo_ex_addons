# -*- coding: utf-8 -*-
# Author : zhy

from odoo import models, fields, api, _
import base64
import sys
from odoo import tools
from odoo.modules.module import get_module_resource

sys.setrecursionlimit(1000000)


class ware_house(models.Model):
    _name = 'ware.house'
    _description = u'编码仓库'

    name = fields.Char(string=u'物料编码')
    cls_one = fields.Char(string=u'所属一级')
    cls_second = fields.Char(string='所属二级')
    date = fields.Datetime(string=u'生成日期', default=fields.Datetime.now, readonly=True)
    desc = fields.Text(string=u'描述')
    ware_id = fields.Many2one('ic.rules', u'编码测试', require=True, track_visibility='onchang')

    attr_s1 = fields.Char(string='参数值1')
    attr_s2 = fields.Char(string='参数值2')
    attr_s3 = fields.Char(string='参数值3')
    attr_s4 = fields.Char(string='参数值4')
    attr_s5 = fields.Char(string='参数值5')


class ic(models.Model, models.BaseModel):
    _name = 'ic.rules'
    _description = u'ic'

    def _default_image(self):
        image_path = get_module_resource('codev2', 'static/src/img', 'default.png')
        return tools.image_process(base64.b64encode(open(image_path, 'rb').read()), size=tools.IMAGE_BIG_SIZE)

    ic_ids = fields.One2many('ware.house', 'ware_id', u'编码明细')
    name = fields.Char(string='物料编码', require=True)
    cls_one = fields.Char(string='一级类型', default='原材料', readonly=True)
    cls_second = fields.Char(string=u'二级类型', default=u'IC', readonly=True)
    cls_type = fields.Selection([
        ('01', '专用IC'),
        ('02', '存储器'),
        ('03', '嵌入式'),
        ('04', '接口'),
        ('05', '数据采集'),
        ('06', '时钟/计时'),
        ('07', '线性'),
        ('08', '逻辑'),
        ('09', '逻辑器件'),
        ('10', '音频专用'),
        ('11', 'PMIC'),
    ], index=True, string=u'类型(三级)', default='01')
    date = fields.Datetime(string='生成日期', default=fields.Datetime.now, readonly=True)
    desc = fields.Text(string=u'物料描述', track_visibility='onchange')
    image = fields.Binary(string=u'图像', default=_default_image, attachment=True)
    image_medium = fields.Binary('Medium', attachment=True)
    image_small = fields.Binary('Thumbnail', attachment=True)
    file_1 = fields.Binary(u"图片上传测试", )
    filename_1 = fields.Char()
    content = fields.Html(string=u'正文', strip_style=True)
    attachment_ids = fields.Many2many('ir.attachment', 'process_attachment_ic_rel', 'process_id', 'attachment_id',
                                      u'附件')
    attr_v1 = fields.Char(string=u'Reference')
    attr_v3 = fields.Char(string=u'Value')
    attr_v4 = fields.Char(string=u'MPN1')
    attr_v5 = fields.Char(string=u'MFR1')
    attr_v6 = fields.Char(string=u'MPN2')
    attr_v7 = fields.Char(string=u'MFR2')
    attr_v8 = fields.Char(string=u'MPN3')
    attr_v9 = fields.Char(string=u'MFR3')
    attr_v10 = fields.Char(string=u'Footprint')
    attr_v11 = fields.Char(string=u'制程类别')
    attr_v12 = fields.Char(string=u'Price')
    attr_v13 = fields.Char(string=u'INSTALL')
    attr_v14 = fields.Selection([
        ('0', 'Pre-release'),
        ('1', 'Approved'),
        ('2', 'Last_Buy'),
        ('3', 'Phase out'),
    ], index=True, string='STATUS', default='0')
    attr_v15 = fields.Char(string=u'Voltage-Supply')
    attr_v16 = fields.Char(string=u'Operating Temperature')

    @api.model
    def create(self, vals):
        if not vals.get('name'):
            level1 = u'3'
            level2 = self._context["default_higher_two_id"]
            level3 = vals.get('cls_type')
            vals['name'] = level1 + level2 + level3 + self.env['ir.sequence'].next_by_code('ic.rules') or '/'
            print(vals['name'])
        res = super(ic, self).create(vals)
        # ic_id = res.write_data()
        return res


class frequency(models.Model, models.BaseModel):
    _name = 'frequency.rules'
    _description = u'频率振荡器'

    def _default_image(self):
        image_path = get_module_resource('codev2', 'static/src/img', 'default.png')
        return tools.image_process(base64.b64encode(open(image_path, 'rb').read()), size=tools.IMAGE_BIG_SIZE)

    name = fields.Char(string=u'物料编码')
    cls_one = fields.Char(string='一级类型', default='原材料', readonly=True)
    cls_second = fields.Char(string=u'二级类型', default=u'频率振荡器', readonly=True)
    date = fields.Datetime(string=u'生成日期', default=fields.Datetime.now, readonly=True)
    desc = fields.Text(string=u'物料描述')
    image = fields.Binary(string=u'图像', default=_default_image, attachment=True)
    image_medium = fields.Binary('Medium', attachment=True)
    image_small = fields.Binary('Thumbnail', attachment=True)
    content = fields.Html(string=u'正文', strip_style=True)
    attachment_ids = fields.Many2many('ir.attachment', 'process_attachment_frequency_rel', 'process_id',
                                      'attachment_id', u'附件')
    attr_v1 = fields.Char(string=u'Reference')
    attr_v3 = fields.Char(string=u'Value')
    attr_v4 = fields.Char(string=u'MPN1')
    attr_v5 = fields.Char(string=u'MFR1')
    attr_v6 = fields.Char(string=u'MPN2')
    attr_v7 = fields.Char(string=u'MFR2')
    attr_v8 = fields.Char(string=u'MPN3')
    attr_v9 = fields.Char(string=u'MFR3')
    attr_v10 = fields.Char(string=u'Footprint')
    attr_v11 = fields.Char(string=u'制程类别')
    attr_v12 = fields.Char(string=u'Price')
    attr_v13 = fields.Char(string=u'INSTALL')
    attr_v14 = fields.Selection([
        ('0', 'Pre-release'),
        ('1', 'Approved'),
        ('2', 'Last_Buy'),
        ('3', 'Phase out'),
    ], index=True, string='STATUS', default='0')
    attr_v15 = fields.Char(string=u'Operating Temperature')
    attr_v16 = fields.Char(string=u'Voltage')
    attr_v17 = fields.Char(string=u'Current')
    attr_v18 = fields.Char(string=u'FS')

    @api.model
    def create(self, vals):
        if not vals.get('name'):
            level1 = u'3'
            level2 = self._context["default_higher_two_id"]
            level3 = u'01'
            vals['name'] = level1 + level2 + level3 + self.env['ir.sequence'].next_by_code('frequency.rules') or '/'
            print(vals['name'])
        res = super(frequency, self).create(vals)
        res.write_data()
        return res

    @api.model
    def write_data(self):
        warehouse = self.env["ware.house"]
        level4 = models.BaseModel.default_get(self, fields_list=['cls_second', 'cls_one'])
        level5 = level4['cls_second']
        level6 = level4['cls_one']
        warehouse.create({
            'name': self.name,
            'cls_one': level6,
            'cls_second': level5,
            'date': self.date,
            'desc': self.desc,
            'attr_v1': self.attr_v1,
            'attr_v3': self.attr_v3,
            'attr_v4': self.attr_v4,
            'attr_v5': self.attr_v5,
        })


class semiconductor(models.Model, models.BaseModel):
    _name = 'semiconductor.rules'
    _description = u'半导体二极管'

    def _default_image(self):
        image_path = get_module_resource('codev2', 'static/src/img', 'default.png')
        return tools.image_process(base64.b64encode(open(image_path, 'rb').read()), size=tools.IMAGE_BIG_SIZE)

    name = fields.Char(string=u'物料编码')
    cls_one = fields.Char(string='一级类型', default='原材料', readonly=True)
    cls_second = fields.Char(string=u'二级类型', default=u'半导体二极管', readonly=True)
    cls_type = fields.Selection([
        ('01', u'发光二极管'),
        ('02', u'肖特基二极管'),
        ('03', u'稳压二极管'),
        ('04', u'变容二极管'),
        ('05', u'TVS二极管'),
    ], index=True, string=u'类型(三级)', default='01')
    date = fields.Datetime(string=u'生成日期', default=fields.Datetime.now, readonly=True)
    desc = fields.Text(string=u'物料描述')
    image = fields.Binary(string=u'图像', default=_default_image, attachment=True)
    image_medium = fields.Binary('Medium', attachment=True)
    image_small = fields.Binary('Thumbnail', attachment=True)
    content = fields.Html(string=u'正文', strip_style=True)
    attachment_ids = fields.Many2many('ir.attachment', 'process_attachment_sem_rel', 'process_id', 'attachment_id',
                                      u'附件')
    attr_v1 = fields.Char(string=u'Reference')
    attr_v3 = fields.Char(string=u'Value')
    attr_v4 = fields.Char(string=u'MPN1')
    attr_v5 = fields.Char(string=u'MFR1')
    attr_v6 = fields.Char(string=u'MPN2')
    attr_v7 = fields.Char(string=u'MFR2')
    attr_v8 = fields.Char(string=u'MPN3')
    attr_v9 = fields.Char(string=u'MFR3')
    attr_v10 = fields.Char(string=u'Footprint')
    attr_v11 = fields.Char(string=u'制程类别')
    attr_v12 = fields.Char(string=u'Price')
    attr_v13 = fields.Char(string=u'INSTALL')
    attr_v14 = fields.Selection([
        ('0', 'Pre-release'),
        ('1', 'Approved'),
        ('2', 'Last_Buy'),
        ('3', 'Phase out'),
    ], index=True, string='STATUS', default='0')
    attr_v15 = fields.Char(string=u'VF')
    attr_v16 = fields.Char(string=u'VR')
    attr_v17 = fields.Char(string=u'IR')
    attr_v18 = fields.Char(string=u'PD')
    attr_v19 = fields.Char(string=u'IF')

    @api.model
    def create(self, vals):
        if not vals.get('name'):
            level1 = u'3'
            level2 = self._context["default_higher_two_id"]
            level3 = vals.get('cls_type')
            vals['name'] = level1 + level2 + level3 + self.env['ir.sequence'].next_by_code('semiconductor.rules') or '/'
            print(vals['name'])
        res = super(semiconductor, self).create(vals)
        res.write_data()
        return res

    @api.model
    def write_data(self):
        warehouse = self.env["ware.house"]
        level4 = models.BaseModel.default_get(self, fields_list=['cls_second', 'cls_one'])
        level5 = level4['cls_second']
        level6 = level4['cls_one']
        warehouse.create({
            'name': self.name,
            'cls_one': level6,
            'cls_second': level5,
            'date': self.date,
            'desc': self.desc,
            'attr_v1': self.attr_v1,
            'attr_v3': self.attr_v3,
            'attr_v4': self.attr_v4,
            'attr_v5': self.attr_v5,
        })


class transistor(models.Model, models.BaseModel):
    _name = 'transistor.rules'
    _description = u'晶体管'

    def _default_image(self):
        image_path = get_module_resource('codev2', 'static/src/img', 'default.png')
        return tools.image_process(base64.b64encode(open(image_path, 'rb').read()), size=tools.IMAGE_BIG_SIZE)

    name = fields.Char(string=u'物料编码')
    cls_one = fields.Char(string='一级类型', default='原材料', readonly=True)
    cls_second = fields.Char(string=u'二级类型', default=u'晶体管', readonly=True)
    cls_type = fields.Selection([
        ('01', u'NPN晶体管'),
        ('02', u'PNP晶体管'),
        ('03', u'达林顿管及复合管'),
        ('04', u'IGBT'),
    ], index=True, string=u'类型(三级)', default='01')
    date = fields.Datetime(string=u'生成日期', default=fields.Datetime.now, readonly=True)
    desc = fields.Text(string=u'物料描述')
    image = fields.Binary(string=u'图像', default=_default_image, attachment=True)
    image_medium = fields.Binary('Medium', attachment=True)
    image_small = fields.Binary('Thumbnail', attachment=True)
    content = fields.Html(string=u'正文', strip_style=True)
    attachment_ids = fields.Many2many('ir.attachment', 'process_attachment_tran_rel', 'process_id', 'attachment_id',
                                      u'附件')
    attr_v1 = fields.Char(string=u'Reference')
    attr_v3 = fields.Char(string=u'Value')
    attr_v4 = fields.Char(string=u'MPN1')
    attr_v5 = fields.Char(string=u'MFR1')
    attr_v6 = fields.Char(string=u'MPN2')
    attr_v7 = fields.Char(string=u'MFR2')
    attr_v8 = fields.Char(string=u'MPN3')
    attr_v9 = fields.Char(string=u'MFR3')
    attr_v10 = fields.Char(string=u'Footprint')
    attr_v11 = fields.Char(string=u'制程类别')
    attr_v12 = fields.Char(string=u'Price')
    attr_v13 = fields.Char(string=u'INSTALL')
    attr_v14 = fields.Selection([
        ('0', 'Pre-release'),
        ('1', 'Approved'),
        ('2', 'Last_Buy'),
        ('3', 'Phase out'),
    ], index=True, string='STATUS', default='0')
    attr_v15 = fields.Char(string=u'Operating Temperature')
    attr_v16 = fields.Char(string=u'VCEO')
    attr_v17 = fields.Char(string=u'PD')
    attr_v18 = fields.Char(string=u'IC')
    attr_v19 = fields.Char(string=u'GAIN')

    @api.model
    def create(self, vals):
        if not vals.get('name'):
            level1 = u'3'
            level2 = self._context["default_higher_two_id"]
            level3 = vals.get('cls_type')
            vals['name'] = level1 + level2 + level3 + self.env['ir.sequence'].next_by_code('transistor.rules') or '/'
            print(vals['name'])
        res = super(transistor, self).create(vals)
        res.write_data()
        return res

    @api.model
    def write_data(self):
        warehouse = self.env["ware.house"]
        level4 = models.BaseModel.default_get(self, fields_list=['cls_second', 'cls_one'])
        level5 = level4['cls_second']
        level6 = level4['cls_one']
        warehouse.create({
            'name': self.name,
            'cls_one': level6,
            'cls_second': level5,
            'date': self.date,
            'desc': self.desc,
            'attr_v1': self.attr_v1,
            'attr_v3': self.attr_v3,
            'attr_v4': self.attr_v4,
            'attr_v5': self.attr_v5,
        })


class mosfet(models.Model, models.BaseModel):
    _name = 'mosfet.rules'
    _description = u'mosfet'

    def _default_image(self):
        image_path = get_module_resource('codev2', 'static/src/img', 'default.png')
        return tools.image_process(base64.b64encode(open(image_path, 'rb').read()), size=tools.IMAGE_BIG_SIZE)

    name = fields.Char(string=u'物料编码')
    cls_one = fields.Char(string='一级类型', default='原材料', readonly=True)
    cls_second = fields.Char(string=u'二级类型', default=u'MOSFET', readonly=True)
    cls_type = fields.Selection([
        ('01', 'P沟道'),
        ('02', 'N沟道'),
        ('03', 'DUAL P沟道'),
        ('04', 'DUAL N沟道'),
    ], index=True, string='类型(三级)', default='01')
    date = fields.Datetime(string='生成日期', default=fields.Datetime.now, readonly=True)
    desc = fields.Text(string='物料描述')
    image = fields.Binary(string='图像', default=_default_image, attachment=True)
    image_medium = fields.Binary('Medium', attachment=True)
    image_small = fields.Binary('Thumbnail', attachment=True)
    content = fields.Html(string=u'正文', strip_style=True)
    attachment_ids = fields.Many2many('ir.attachment', 'process_attachment_mosfet_rel', 'process_id', 'attachment_id',
                                      u'附件')
    attr_v1 = fields.Char(string='Reference')
    attr_v3 = fields.Char(string='Value')
    attr_v4 = fields.Char(string='MPN1')
    attr_v5 = fields.Char(string='MFR1')
    attr_v6 = fields.Char(string='MPN2')
    attr_v7 = fields.Char(string='MFR2')
    attr_v8 = fields.Char(string='MPN3')
    attr_v9 = fields.Char(string='MFR3')
    attr_v10 = fields.Char(string='Footprint')
    attr_v11 = fields.Char(string='制程类别')
    attr_v12 = fields.Char(string='Price')
    attr_v13 = fields.Char(string='INSTALL')
    attr_v14 = fields.Selection([
        ('0', 'Pre-release'),
        ('1', 'Approved'),
        ('2', 'Last_Buy'),
        ('3', 'Phase out'),
    ], index=True, string='STATUS', default='0')
    attr_v15 = fields.Char(string='VDS')
    attr_v16 = fields.Char(string='RDS(ON)')
    attr_v17 = fields.Char(string='VGS')
    attr_v18 = fields.Char(string='VGS(th)')

    @api.model
    def create(self, vals):
        if not vals.get('name'):
            level1 = u'3'
            level2 = self._context["default_higher_two_id"]
            level3 = vals.get('cls_type')
            vals['name'] = level1 + level2 + level3 + self.env['ir.sequence'].next_by_code('mosfet.rules') or '/'
            print(vals['name'])
        return super(mosfet, self).create(vals)

    @api.model
    def write_data(self):
        warehouse = self.env["ware.house"]
        level4 = models.BaseModel.default_get(self, fields_list=['cls_second', 'cls_one'])
        level5 = level4['cls_second']
        level6 = level4['cls_one']
        warehouse.create({
            'name': self.name,
            'cls_one': level6,
            'cls_second': level5,
            'date': self.date,
            'desc': self.desc,
            'attr_v1': self.attr_v1,
            'attr_v3': self.attr_v3,
            'attr_v4': self.attr_v4,
            'attr_v5': self.attr_v5,
        })


class capacitance(models.Model, models.BaseModel):
    _name = 'capacitance.rules'
    _description = u'电容'

    def _default_image(self):
        image_path = get_module_resource('codev2', 'static/src/img', 'default.png')
        return tools.image_process(base64.b64encode(open(image_path, 'rb').read()), size=tools.IMAGE_BIG_SIZE)

    name = fields.Char(string=u'物料编码')
    cls_one = fields.Char(string='一级类型', default='原材料', readonly=True)
    cls_second = fields.Char(string=u'二级类型', default=u'电容', readonly=True)
    cls_type = fields.Selection([
        ('01', u'陶瓷电容'),
        ('02', u'钽电容'),
        ('03', u'电解电容'),
        ('04', u'云母电容'),
        ('05', u'聚酯电容'),
        ('06', u'可变电容'),
    ], index=True, string=u'类型(三级)', default='01')
    date = fields.Datetime(string='生成日期', default=fields.Datetime.now, readonly=True)
    desc = fields.Text(string=u'物料描述')
    image = fields.Binary(string=u'图像', default=_default_image, attachment=True)
    image_medium = fields.Binary('Medium', attachment=True)
    image_small = fields.Binary('Thumbnail', attachment=True)
    content = fields.Html(string=u'正文', strip_style=True)
    attachment_ids = fields.Many2many('ir.attachment', 'process_attachment_capa_rel', 'process_id', 'attachment_id',
                                      u'附件')
    attr_v1 = fields.Char(string=u'Reference')
    attr_v3 = fields.Char(string=u'Value')
    attr_v4 = fields.Char(string=u'MPN1')
    attr_v5 = fields.Char(string=u'MFR1')
    attr_v6 = fields.Char(string=u'MPN2')
    attr_v7 = fields.Char(string=u'MFR2')
    attr_v8 = fields.Char(string=u'MPN3')
    attr_v9 = fields.Char(string=u'MFR3')
    attr_v10 = fields.Char(string=u'Footprint')
    attr_v11 = fields.Char(string=u'制成类别')
    attr_v12 = fields.Char(string=u'Price')
    attr_v13 = fields.Char(string=u'INSTALL')
    attr_v14 = fields.Selection([
        ('0', 'Pre-release'),
        ('1', 'Approved'),
        ('2', 'Last_Buy'),
        ('3', 'Phase out'),
    ], index=True, string='STATUS', default='0')
    attr_v15 = fields.Char(string=u'Voltage')
    attr_v16 = fields.Char(string=u'Tolorance')
    attr_v17 = fields.Char(string=u'Operating Temperature')

    @api.model
    def create(self, vals):
        if not vals.get('name'):
            level1 = u'3'
            level2 = self._context["default_higher_two_id"]
            level3 = vals.get('cls_type')
            vals['name'] = level1 + level2 + level3 + self.env['ir.sequence'].next_by_code('capacitance.rules') or '/'
            print(vals['name'])
        res = super(capacitance, self).create(vals)
        res.write_data()
        return res

    @api.model
    def write_data(self):
        warehouse = self.env["ware.house"]
        level4 = models.BaseModel.default_get(self, fields_list=['cls_second', 'cls_one'])
        level5 = level4['cls_second']
        level6 = level4['cls_one']
        warehouse.create({
            'name': self.name,
            'cls_one': level6,
            'cls_second': level5,
            'date': self.date,
            'desc': self.desc,
            'attr_v1': self.attr_v1,
            # 'attr_v2': self.attr_v2,
            'attr_v3': self.attr_v3,
            'attr_v4': self.attr_v4,
            'attr_v5': self.attr_v5,
        })


class resistance(models.Model, models.BaseModel):
    _name = 'resistance.rules'
    _description = u'电阻'

    def _default_image(self):
        image_path = get_module_resource('codev2', 'static/src/img', 'default.png')
        return tools.image_process(base64.b64encode(open(image_path, 'rb').read()), size=tools.IMAGE_BIG_SIZE)

    name = fields.Char(string=u'物料编码')
    cls_one = fields.Char(string='一级类型', default='原材料', readonly=True)
    cls_second = fields.Char(string=u'二级类型', default="电阻", readonly=True)
    cls_type = fields.Selection([
        ('01', u'碳膜电阻'),
        ('02', u'金属膜电阻'),
        ('03', u'线绕电阻'),
        ('04', u'水泥电阻'),
        ('05', u'排电阻'),
        ('06', u'可变电阻')
    ], index=True, string=u'类型(三级)', default='01')
    date = fields.Datetime(string=u'生成日期', default=fields.Datetime.now, readonly=True)
    desc = fields.Text(string=u'物料描述')
    # order_id = fields.Many2one('ware.house', string=u'属性表', require=True, ondelete='cascade', index=True, copy=False)
    image = fields.Binary(string=u'图像', default=_default_image, attachment=True)
    image_medium = fields.Binary('Medium', attachment=True)
    image_small = fields.Binary('Thumbnail', attachment=True)
    content = fields.Html(string=u'正文', strip_style=True)
    attachment_ids = fields.Many2many('ir.attachment', 'process_attachment_resis_rel', 'process_id', 'attachment_id',
                                      u'附件')
    attr_v1 = fields.Char(string=u'Reference')
    attr_v3 = fields.Char(string=u'Value')
    attr_v4 = fields.Char(string=u'MPN1')
    attr_v5 = fields.Char(string=u'MFR1')
    attr_v6 = fields.Char(string=u'MPN2')
    attr_v7 = fields.Char(string=u'MFR2')
    attr_v8 = fields.Char(string=u'MPN3')
    attr_v9 = fields.Char(string=u'MFR3')
    attr_v10 = fields.Char(string=u'Footprint')
    attr_v11 = fields.Char(string=u'制程类别')
    attr_v12 = fields.Char(string=u'Price')
    attr_v13 = fields.Char(string=u'INSTALL')
    attr_v14 = fields.Selection([
        ('0', 'Pre-release'),
        ('1', 'Approved'),
        ('2', 'Last_Buy'),
        ('3', 'Phase out'),
    ], index=True, string='STATUS', default='0')
    attr_v15 = fields.Char(string=u'Tolorance')
    attr_v16 = fields.Char(string=u'PWR')
    attr_v17 = fields.Char(string=u'Temperature Coefficient')
    attr_v18 = fields.Char(string=u'Operating Temperature')

    @api.model
    def create(self, vals):
        if not vals.get('name'):
            level1 = u'3'
            level2 = self._context["default_higher_two_id"]
            level3 = vals.get('cls_type')
            print(level2, level3, 3333333333, type(level1), type(level2), type(level3))
            vals['name'] = level1 + level2 + level3 + self.env['ir.sequence'].next_by_code('resistance.rules') or '/'
            print(vals['name'])
        res = super(resistance, self).create(vals)
        res.write_data()
        return res

    @api.model
    def write_data(self):
        warehouse = self.env["ware.house"]
        level4 = models.BaseModel.default_get(self, fields_list=['cls_second', 'cls_one'])
        level5 = level4['cls_second']
        level6 = level4['cls_one']
        warehouse.create({
            'name': self.name,
            'cls_one': level6,
            'cls_second': level5,
            'date': self.date,
            'desc': self.desc,
            'attr_v1': self.attr_v1,
            'attr_v3': self.attr_v3,
            'attr_v4': self.attr_v4,
            'attr_v5': self.attr_v5,
        })


class inductance(models.Model, models.BaseModel):
    _name = 'inductance.rules'
    _description = u'电感'

    def _default_image(self):
        image_path = get_module_resource('codev2', 'static/src/img', 'default.png')
        return tools.image_process(base64.b64encode(open(image_path, 'rb').read()), size=tools.IMAGE_BIG_SIZE)

    name = fields.Char(string=u'物料编码')
    cls_one = fields.Char(string='一级类型', default='原材料', readonly=True)
    cls_second = fields.Char(string=u'二级类型', default=u'电感', readonly=True)
    cls_type = fields.Selection([
        ('01', u'DIP'),
        ('02', u'SMD'),
        ('03', u'磁珠'),
        ('04', u'磁环'),
    ], index=True, string=u'类型(三级)', default='01')
    date = fields.Datetime(string=u'生成日期', default=fields.Datetime.now, readonly=True)
    desc = fields.Text(string=u'物料描述')
    image = fields.Binary(string=u'图像', default=_default_image, attachment=True)
    image_medium = fields.Binary('Medium', attachment=True)
    image_small = fields.Binary('Thumbnail', attachment=True)
    content = fields.Html(string=u'正文', strip_style=True)
    attachment_ids = fields.Many2many('ir.attachment', 'process_attachment_induc_rel', 'process_id', 'attachment_id',
                                      u'附件')
    attr_v1 = fields.Char(string=u'Reference')
    attr_v3 = fields.Char(string=u'Value')
    attr_v4 = fields.Char(string=u'MPN1')
    attr_v5 = fields.Char(string=u'MFR1')
    attr_v6 = fields.Char(string=u'MPN2')
    attr_v7 = fields.Char(string=u'MFR2')
    attr_v8 = fields.Char(string=u'MPN3')
    attr_v9 = fields.Char(string=u'MFR3')
    attr_v10 = fields.Char(string=u'Footprint')
    attr_v11 = fields.Char(string=u'制程类别')
    attr_v12 = fields.Char(string=u'Price')
    attr_v13 = fields.Char(string=u'INSTALL')
    attr_v14 = fields.Selection([
        ('0', 'Pre-release'),
        ('1', 'Approved'),
        ('2', 'Last_Buy'),
        ('3', 'Phase out'),
    ], index=True, string='STATUS', default='0')
    attr_v15 = fields.Char(string=u'Footprint Ref')

    @api.model
    def create(self, vals):
        if not vals.get('name'):
            level1 = u'3'
            level2 = self._context["default_higher_two_id"]
            level3 = vals.get('cls_type')
            vals['name'] = level1 + level2 + level3 + self.env['ir.sequence'].next_by_code('inductance.rules') or '/'
            print(vals['name'])
        res = super(inductance, self).create(vals)
        res.write_data()
        return res

    @api.model
    def write_data(self):
        warehouse = self.env["ware.house"]
        level4 = models.BaseModel.default_get(self, fields_list=['cls_second', 'cls_one'])
        level5 = level4['cls_second']
        level6 = level4['cls_one']
        warehouse.create({
            'name': self.name,
            'cls_one': level6,
            'cls_second': level5,
            'date': self.date,
            'desc': self.desc,
            'attr_v1': self.attr_v1,
            'attr_v3': self.attr_v3,
            'attr_v4': self.attr_v4,
            'attr_v5': self.attr_v5,
        })


class insurance(models.Model, models.BaseModel):
    _name = 'insurance.rules'
    _description = u'保险'

    def _default_image(self):
        image_path = get_module_resource('codev2', 'static/src/img', 'default.png')
        return tools.image_process(base64.b64encode(open(image_path, 'rb').read()), size=tools.IMAGE_BIG_SIZE)

    name = fields.Char(string=u'物料编码')
    cls_one = fields.Char(string='一级类型', default='原材料', readonly=True)
    cls_second = fields.Char(string=u'二级类型', default=u'保险', readonly=True)
    cls_type = fields.Selection([
        ('01', '自恢复'),
        ('02', '不可恢复'),
    ], index=True, string=u'类型(三级)', default='01')
    date = fields.Datetime(string=u'生成日期', default=fields.Datetime.now, readonly=True)
    desc = fields.Text(string=u'物料描述')
    image = fields.Binary(string=u'图像', default=_default_image, attachment=True)
    image_medium = fields.Binary('Medium', attachment=True)
    image_small = fields.Binary('Thumbnail', attachment=True)
    content = fields.Html(string=u'正文', strip_style=True)
    attachment_ids = fields.Many2many('ir.attachment', 'process_attachment_insurance_rel', 'process_id',
                                      'attachment_id', u'附件')
    attr_v1 = fields.Char(string=u'Reference')
    attr_v3 = fields.Char(string=u'Value')
    attr_v4 = fields.Char(string=u'MPN1')
    attr_v5 = fields.Char(string=u'MFR1')
    attr_v6 = fields.Char(string=u'MPN2')
    attr_v7 = fields.Char(string=u'MFR2')
    attr_v8 = fields.Char(string=u'MPN3')
    attr_v9 = fields.Char(string=u'MFR3')
    attr_v10 = fields.Char(string=u'Footprint')
    attr_v11 = fields.Char(string=u'制程类别')
    attr_v12 = fields.Char(string=u'Price')
    attr_v13 = fields.Char(string=u'INSTALL')
    attr_v14 = fields.Selection([
        ('0', 'Pre_rebease'),
        ('1', 'Approved'),
        ('2', 'Last_Buy'),
        ('3', 'Phaseont'),
    ], index=True, string='STATUS', default='0')
    attr_v15 = fields.Char(string=u'RC')
    attr_v16 = fields.Char(string=u'DCR')
    attr_v17 = fields.Char(string=u'Voltage-Supply')

    @api.model
    def create(self, vals):
        if not vals.get('name'):
            level1 = u'3'
            level2 = self._context["default_higher_two_id"]
            level3 = vals.get('cls_type')
            vals['name'] = level1 + level2 + level3 + self.env['ir.sequence'].next_by_code('insurance.rules') or '/'
            print(vals['name'])
        res = super(insurance, self).create(vals)
        res.write_data()
        return res

    @api.model
    def write_data(self):
        warehouse = self.env["ware.house"]
        level4 = models.BaseModel.default_get(self, fields_list=['cls_second', 'cls_one'])
        level5 = level4['cls_second']
        level6 = level4['cls_one']
        warehouse.create({
            'name': self.name,
            'cls_one': level6,
            'cls_second': level5,
            'date': self.date,
            'desc': self.desc,
            'attr_v1': self.attr_v1,
            'attr_v3': self.attr_v3,
            'attr_v4': self.attr_v4,
            'attr_v5': self.attr_v5,
        })


class connectors(models.Model, models.BaseModel):
    _name = 'connectors.rules'
    _description = u'连接器'

    def _default_image(self):
        image_path = get_module_resource('codev2', 'static/src/img', 'default.png')
        return tools.image_process(base64.b64encode(open(image_path, 'rb').read()), size=tools.IMAGE_BIG_SIZE)

    name = fields.Char(string=u'物料编码')
    cls_one = fields.Char(string='一级类型', default='原材料', readonly=True)
    cls_second = fields.Char(string=u'二级类型', default=u'连接器', readonly=True)
    date = fields.Datetime(string=u'生成日期', default=fields.Datetime.now, readonly=True)
    desc = fields.Text(string=u'物料描述')
    image = fields.Binary(string=u'图像', default=_default_image, attachment=True)
    image_medium = fields.Binary('Medium', attachment=True)
    image_small = fields.Binary('Thumbnail', attachment=True)
    content = fields.Html(string=u'正文', strip_style=True)
    attachment_ids = fields.Many2many('ir.attachment', 'process_attachment_connectors_rel', 'process_id',
                                      'attachment_id', u'附件')
    attr_v1 = fields.Char(string=u'Reference')
    attr_v3 = fields.Char(string=u'Value')
    attr_v4 = fields.Char(string=u'MPN1')
    attr_v5 = fields.Char(string=u'MFR1')
    attr_v6 = fields.Char(string=u'MPN2')
    attr_v7 = fields.Char(string=u'MFR2')
    attr_v8 = fields.Char(string=u'MPN3')
    attr_v9 = fields.Char(string=u'MFR3')
    attr_v10 = fields.Char(string=u'Footprint')
    attr_v11 = fields.Char(string=u'制程类别')
    attr_v12 = fields.Char(string=u'Price')
    attr_v13 = fields.Char(string=u'INSTALL')
    attr_v14 = fields.Selection([
        ('0', 'Pre-release'),
        ('1', 'Approved'),
        ('2', 'Last_Buy'),
        ('3', 'Phase out'),
    ], index=True, string='STATUS', default='0')

    @api.model
    def create(self, vals):
        if not vals.get('name'):
            level1 = u'3'
            level2 = self._context["default_higher_two_id"]
            level3 = u'01'
            vals['name'] = level1 + level2 + level3 + self.env['ir.sequence'].next_by_code('connectors.rules') or '/'
            print(vals['name'])
        res = super(connectors, self).create(vals)
        res.write_data()
        return res

    @api.model
    def write_data(self):
        warehouse = self.env["ware.house"]
        level4 = models.BaseModel.default_get(self, fields_list=['cls_second', 'cls_one'])
        level5 = level4['cls_second']
        level6 = level4['cls_one']
        warehouse.create({
            'name': self.name,
            'cls_one': level6,
            'cls_second': level5,
            'date': self.date,
            'desc': self.desc,
            'attr_v1': self.attr_v1,
            'attr_v3': self.attr_v3,
            'attr_v4': self.attr_v4,
            'attr_v5': self.attr_v5,
        })


class relay(models.Model, models.BaseModel):
    _name = 'relay.rules'
    _description = u'继电器'

    def _default_image(self):
        image_path = get_module_resource('codev2', 'static/src/img', 'default.png')
        return tools.image_process(base64.b64encode(open(image_path, 'rb').read()), size=tools.IMAGE_BIG_SIZE)

    name = fields.Char(string=u'物料编码')
    cls_one = fields.Char(string='一级类型', default='原材料', readonly=True)
    cls_second = fields.Char(string=u'二级类型', default=u'继电器', readonly=True)
    date = fields.Datetime(string=u'生成日期', default=fields.Datetime.now, readonly=True)
    desc = fields.Text(string=u'物料描述')
    image = fields.Binary(string=u'图像', default=_default_image, attachment=True)
    image_medium = fields.Binary('Medium', attachment=True)
    image_small = fields.Binary('Thumbnail', attachment=True)
    content = fields.Html(string=u'正文', strip_style=True)
    attachment_ids = fields.Many2many('ir.attachment', 'process_attachment_relay_rel', 'process_id', 'attachment_id',
                                      u'附件')
    attr_v1 = fields.Char(string=u'Reference')
    attr_v3 = fields.Char(string=u'Value')
    attr_v4 = fields.Char(string=u'MPN1')
    attr_v5 = fields.Char(string=u'MFR1')
    attr_v6 = fields.Char(string=u'MPN2')
    attr_v7 = fields.Char(string=u'MFR2')
    attr_v8 = fields.Char(string=u'MPN3')
    attr_v9 = fields.Char(string=u'MFR3')
    attr_v10 = fields.Char(string=u'Footprint')
    attr_v11 = fields.Char(string=u'制程类别')
    attr_v12 = fields.Char(string=u'Price')
    attr_v13 = fields.Char(string=u'INSTALL')
    attr_v14 = fields.Selection([
        ('0', 'Pre-release'),
        ('1', 'Approved'),
        ('2', 'Last_Buy'),
        ('3', 'Phase out'),
    ], index=True, string='STATUS', default='0')
    attr_v15 = fields.Char(string=u'CV')
    attr_v16 = fields.Char(string=u'CR')
    attr_v17 = fields.Char(string=u'TYPE')
    attr_v18 = fields.Char(string=u'MSV')
    attr_v19 = fields.Char(string=u'MSC')

    @api.model
    def create(self, vals):
        if not vals.get('name'):
            level1 = u'3'
            level2 = self._context["default_higher_two_id"]
            level3 = u'01'
            vals['name'] = level1 + level2 + level3 + self.env['ir.sequence'].next_by_code('relay.rules') or '/'
            print(vals['name'])
        res = super(relay, self).create(vals)
        res.write_data()
        return res

    @api.model
    def write_data(self):
        warehouse = self.env["ware.house"]
        level4 = models.BaseModel.default_get(self, fields_list=['cls_second', 'cls_one'])
        level5 = level4['cls_second']
        level6 = level4['cls_one']
        warehouse.create({
            'name': self.name,
            'cls_one': level6,
            'cls_second': level5,
            'date': self.date,
            'desc': self.desc,
            'attr_v1': self.attr_v1,
            'attr_v3': self.attr_v3,
            'attr_v4': self.attr_v4,
            'attr_v5': self.attr_v5,
        })


class converter(models.Model, models.BaseModel):
    _name = 'converter.rules'
    _description = u'变压器'

    def _default_image(self):
        image_path = get_module_resource('codev2', 'static/src/img', 'default.png')
        return tools.image_process(base64.b64encode(open(image_path, 'rb').read()), size=tools.IMAGE_BIG_SIZE)

    name = fields.Char(string=u'物料编码')
    cls_one = fields.Char(string='一级类型', default='原材料', readonly=True)
    cls_second = fields.Char(string=u'二级类型', default=u'变压器', readonly=True)
    date = fields.Datetime(string=u'生成日期', default=fields.Datetime.now, readonly=True)
    desc = fields.Text(string=u'物料描述')
    image = fields.Binary(string=u'图像', default=_default_image, attachment=True)
    image_medium = fields.Binary('Medium', attachment=True)
    image_small = fields.Binary('Thumbnail', attachment=True)
    content = fields.Html(string=u'正文', strip_style=True)
    attachment_ids = fields.Many2many('ir.attachment', 'process_attachment_converter_rel', 'process_id',
                                      'attachment_id', u'附件')
    attr_v1 = fields.Char(string=u'Reference')
    attr_v3 = fields.Char(string=u'Value')
    attr_v4 = fields.Char(string=u'MPN1')
    attr_v5 = fields.Char(string=u'MFR1')
    attr_v6 = fields.Char(string=u'MPN2')
    attr_v7 = fields.Char(string=u'MFR2')
    attr_v8 = fields.Char(string=u'MPN3')
    attr_v9 = fields.Char(string=u'MFR3')
    attr_v10 = fields.Char(string=u'Footprint')
    attr_v11 = fields.Char(string=u'制程类别')
    attr_v12 = fields.Char(string=u'Price')
    attr_v13 = fields.Char(string=u'INSTALL')
    attr_v14 = fields.Selection([
        ('0', 'Pre-release'),
        ('1', 'Approved'),
        ('2', 'Last_Buy'),
        ('3', 'Phase out'),
    ], index=True, string='STATUS', default='0')
    attr_v15 = fields.Char(string=u'Voltage-Supply')
    attr_v16 = fields.Char(string=u'Operating Temperature')
    attr_v17 = fields.Char(string=u'PD')

    @api.model
    def create(self, vals):
        if not vals.get('name'):
            level1 = u'3'
            level2 = self._context["default_higher_two_id"]
            level3 = u'01'
            vals['name'] = level1 + level2 + level3 + self.env['ir.sequence'].next_by_code('converter.rules') or '/'
            print(vals['name'])
        res = super(converter, self).create(vals)
        res.write_data()
        return res

    @api.model
    def write_data(self):
        warehouse = self.env["ware.house"]
        level4 = models.BaseModel.default_get(self, fields_list=['cls_second', 'cls_one'])
        level5 = level4['cls_second']
        level6 = level4['cls_one']
        warehouse.create({
            'name': self.name,
            'cls_one': level6,
            'cls_second': level5,
            'date': self.date,
            'desc': self.desc,
            'attr_v1': self.attr_v1,
            'attr_v3': self.attr_v3,
            'attr_v4': self.attr_v4,
            'attr_v5': self.attr_v5,
        })


class crystal(models.Model, models.BaseModel):
    _name = 'crystal.rules'
    _description = u'晶体'

    def _default_image(self):
        image_path = get_module_resource('codev2', 'static/src/img', 'default.png')
        return tools.image_process(base64.b64encode(open(image_path, 'rb').read()), size=tools.IMAGE_BIG_SIZE)

    name = fields.Char(string=u'物料编码')
    cls_one = fields.Char(string='一级类型', default='原材料', readonly=True)
    cls_second = fields.Char(string=u'二级类型', default=u'晶体', readonly=True)
    date = fields.Datetime(string=u'生成日期', default=fields.Datetime.now, readonly=True)
    desc = fields.Text(string=u'物料描述')
    image = fields.Binary(string=u'图像', default=_default_image, attachment=True)
    image_medium = fields.Binary('Medium', attachment=True)
    image_small = fields.Binary('Thumbnail', attachment=True)
    content = fields.Html(string=u'正文', strip_style=True)
    attachment_ids = fields.Many2many('ir.attachment', 'process_attachment_crystal_rel', 'process_id', 'attachment_id',
                                      u'附件')
    attr_v1 = fields.Char(string=u'Reference')
    attr_v3 = fields.Char(string=u'Value')
    attr_v4 = fields.Char(string=u'MPN1')
    attr_v5 = fields.Char(string=u'MFR1')
    attr_v6 = fields.Char(string=u'MPN2')
    attr_v7 = fields.Char(string=u'MFR2')
    attr_v8 = fields.Char(string=u'MPN3')
    attr_v9 = fields.Char(string=u'MFR3')
    attr_v10 = fields.Char(string=u'Footprint')
    attr_v11 = fields.Char(string=u'制程类别')
    attr_v12 = fields.Char(string=u'Price')
    attr_v13 = fields.Char(string=u'INSTALL')
    attr_v14 = fields.Selection([
        ('0', 'Pre-release'),
        ('1', 'Approved'),
        ('2', 'Last_Buy'),
        ('3', 'Phase out'),
    ], index=True, string='STATUS', default='0')
    attr_v15 = fields.Char(string=u'Operating Temperature')
    attr_v16 = fields.Char(string=u'FT')
    attr_v17 = fields.Char(string=u'FS')
    attr_v18 = fields.Char(string=u'LC')
    attr_v19 = fields.Char(string=u'ESR')

    @api.model
    def create(self, vals):
        if not vals.get('name'):
            level1 = u'3'
            level2 = self._context["default_higher_two_id"]
            level3 = u'01'
            vals['name'] = level1 + level2 + level3 + self.env['ir.sequence'].next_by_code('crystal.rules') or '/'
            print(vals['name'])
        res = super(crystal, self).create(vals)
        res.write_data()
        return res

    @api.model
    def write_data(self):
        warehouse = self.env["ware.house"]
        level4 = models.BaseModel.default_get(self, fields_list=['cls_second', 'cls_one'])
        level5 = level4['cls_second']
        level6 = level4['cls_one']
        warehouse.create({
            'name': self.name,
            'cls_one': level6,
            'cls_second': level5,
            'date': self.date,
            'desc': self.desc,
            'attr_v1': self.attr_v1,
            # 'attr_v2': self.attr_v2,
            'attr_v3': self.attr_v3,
            'attr_v4': self.attr_v4,
            'attr_v5': self.attr_v5,
        })


class pcba(models.Model, models.BaseModel):
    _name = 'pcba.rules'
    _description = u'pcba'

    def _default_image(self):
        image_path = get_module_resource('codev2', 'static/src/img', 'default.png')
        return tools.image_process(base64.b64encode(open(image_path, 'rb').read()), size=tools.IMAGE_BIG_SIZE)

    name = fields.Char(string=u'物料编码')
    cls_one = fields.Char(string='一级类型', default='半成品', readonly=True)
    cls_second = fields.Char(string=u'二级类型', default=u'pcba', readonly=True)
    date = fields.Datetime(string=u'生成日期', default=fields.Datetime.now, readonly=True)
    desc = fields.Text(string=u'描述')
    content = fields.Html(string=u'正文', strip_style=True)
    # 上传图片 attachment=True表示作为附件上传
    image = fields.Binary(string=u'图像', default=_default_image, attachment=True)
    image_medium = fields.Binary('Medium', attachment=True)
    image_small = fields.Binary('Thumbnail', attachment=True)
    # 图片上传测试
    file_1 = fields.Binary(u"图片上传测试", )
    filename_1 = fields.Char()
    attachment_ids = fields.Many2many('ir.attachment', 'process_attachment_pcba_rel', 'process_id', 'attachment_id',
                                      u'附件')
    attr_v1 = fields.Char(string=u'半成品名称')
    attr_v2 = fields.Selection([
        ('4A', '4A'),
        ('6A', '6A'),
        ('C型', 'C型'),
        ('CZ2', 'CZ2'),
        ('CCU', 'CCU'),
        ('CRH3', 'CRH3'),
        ('显示屏', '显示屏'),
        ('350标动', '350标动'),
        ('400标动', '400标动'),
        ('TKD401B', 'TKD401B'),
        ('深圳地铁', '深圳地铁'),
        ('平谷地铁', '平谷地铁'),
        ('上海地铁', '上海地铁'),
        ('南车IOM', '南车IOM'),
        ('神华机车', '神华机车'),
        ('南车无线传输', '南车无线传输'),
        ('IOM高压单元', 'IOM高压单元'),
    ], index=True, string='项目')
    attr_v3 = fields.Selection([
        ('艾博唯', '艾博唯'),
        ('鼎和信', '鼎和信'),
        ('艾尼克斯', '艾尼克斯'),
        ('精密电产', '精密电产'),
        ('新兴基业', '新兴基业'),
        ('中航科电', '中航科电'),
        ('纵横机电', '纵横机电'),
        ('鼎和信/艾尼克斯', '鼎和信/艾尼克斯'),
        ('中航科电/鼎和信', '中航科电/鼎和信'),
        ('中航科电/鼎和信/艾尼克斯', '中航科电/鼎和信/艾尼克斯'),
    ], index=True, string='供应商')
    attr_v4 = fields.Selection([
        ('有铅', '有铅'),
        ('无铅', '无铅'),
    ], index=True, string='焊接工艺')
    attr_v5 = fields.Selection([
        ('有机硅', '有机硅'),
        ('丙烯酸', '丙烯酸'),
    ], index=True, string='三防漆')
    attr_v6 = fields.Char(string=u'软件版本')

    @api.model
    def create(self, vals):
        # tools.image_resize_images(vals)
        if not vals.get('name'):
            level1 = u'2'
            level2 = self._context["default_higher_two_id"]
            level3 = u'00'
            vals['name'] = level1 + level2 + level3 + self.env['ir.sequence'].next_by_code('pcba.rules') or '/'
            print(vals['name'])
        res = super(pcba, self).create(vals)
        res.write_data()
        return res

    @api.model
    def write_data(self):
        warehouse = self.env["ware.house"]
        level4 = models.BaseModel.default_get(self, fields_list=['cls_second', 'cls_one'])
        level5 = level4['cls_second']
        level6 = level4['cls_one']
        warehouse.create({
            'name': self.name,
            'cls_one': level6,
            'cls_second': level5,
            'date': self.date,
            'desc': self.desc,
            'attr_v1': self.attr_v1,
            'attr_v2': self.attr_v2,
            'attr_v3': self.attr_v3,
            'attr_v4': self.attr_v4,
            'attr_v5': self.attr_v5,
        })


class machine(models.Model, models.BaseModel):
    _name = 'machine.rules'
    _description = u'整机'

    def _default_image(self):
        image_path = get_module_resource('codev2', 'static/src/img', 'default.png')
        return tools.image_process(base64.b64encode(open(image_path, 'rb').read()), size=tools.IMAGE_BIG_SIZE)

    name = fields.Char(string=u'物料编码')
    cls_one = fields.Char(string='一级类型', default='完成品', readonly=True)
    cls_second = fields.Char(string=u'二级类型', default=u'整机', readonly=True)
    cls_type = fields.Selection([
        ('01', u'完全外采'),
        ('02', u'含自制产品整机'),
    ], index=True, string='类型编码', default='01')
    date = fields.Datetime(string=u'生成日期', default=fields.Datetime.now, readonly=True)
    desc = fields.Text(string='物料描述')
    image = fields.Binary(string=u'图像', default=_default_image, attachment=True)
    image_medium = fields.Binary('Medium', attachment=True)
    image_small = fields.Binary('Thumbnail', attachment=True)
    content = fields.Html(string=u'正文', strip_style=True)
    attachment_ids = fields.Many2many('ir.attachment', 'process_attachment_machine_rel', 'process_id', 'attachment_id',
                                      u'附件')
    attr_s1 = fields.Char(string='物料名称')
    attr_v1 = fields.Char(string='软件名称及版本信息')
    attr_v2 = fields.Char(string='PCB-BOM文件名称及版本')
    attr_v3 = fields.Char(string='PCB工程文件名称及版本')
    attr_v4 = fields.Char(string='项目')
    attr_v5 = fields.Char(string='责任工程师')
    attr_v6 = fields.Char(string='客户物料号')
    attr_v8 = fields.Char(string='客户图号')
    attr_v9 = fields.Char(string='品牌')

    @api.model
    def create(self, vals):
        if not vals.get('name'):
            level1 = '1'
            level2 = self._context["default_higher_two_id"]
            level3 = vals.get('cls_type')
            vals['name'] = level1 + level2 + level3 + self.env['ir.sequence'].next_by_code('machine.rules') or '/'
            print(vals['name'])
        res = super(machine, self).create(vals)
        res.write_data()
        return res

    @api.model
    def write_data(self):
        warehouse = self.env["ware.house"]
        level4 = models.BaseModel.default_get(self, fields_list=['cls_second', 'cls_one'])
        level5 = level4['cls_second']
        level6 = level4['cls_one']
        warehouse.create({
            'name': self.name,
            'cls_one': level6,
            'cls_second': level5,
            'date': self.date,
            'desc': self.desc,
            'attr_v1': self.attr_v1,
            'attr_v2': self.attr_v2,
            'attr_v3': self.attr_v3,
            'attr_v4': self.attr_v4,
            'attr_v5': self.attr_v5,
        })


class mymodule(models.Model, models.BaseModel):
    _name = 'mymodule.rules'
    _description = u'模块'

    def _default_image(self):
        image_path = get_module_resource('codev2', 'static/src/img', 'default.png')
        return tools.image_process(base64.b64encode(open(image_path, 'rb').read()), size=tools.IMAGE_BIG_SIZE)

    name = fields.Char(string=u'物料编码')
    cls_one = fields.Char(string='一级类型', default='完成品', readonly=True)
    cls_second = fields.Char(string=u'二级类型', default=u'模块', readonly=True)
    cls_type = fields.Selection([
        ('01', u'完全外采'),
        ('02', u'含自制产品整机'),
    ], index=True, string='类型编码', default='01')
    date = fields.Datetime(string=u'生成日期', default=fields.Datetime.now, readonly=True)
    desc = fields.Text(string='描述信息')
    image = fields.Binary(string=u'图像', default=_default_image, attachment=True)
    image_medium = fields.Binary('Medium', attachment=True)
    image_small = fields.Binary('Thumbnail', attachment=True)
    content = fields.Html(string=u'正文', strip_style=True)
    attachment_ids = fields.Many2many('ir.attachment', 'process_attachment_mymodule_rel', 'process_id', 'attachment_id',
                                      u'附件')
    attr_s1 = fields.Char(string='物料名称')
    attr_v1 = fields.Char(string='软件名称及版本信息')
    attr_v2 = fields.Char(string='PCB-BOM文件名称及版本')
    attr_v3 = fields.Char(string='PCB工程文件名称及版本')
    attr_v4 = fields.Char(string='项目')
    attr_v5 = fields.Char(string='责任工程师')
    attr_v6 = fields.Char(string='客户物料号')
    attr_v7 = fields.Char(string='物料描述')
    attr_v8 = fields.Char(string='客户图号')
    attr_v9 = fields.Char(string='品牌')

    @api.model
    def create(self, vals):
        if not vals.get('name'):
            level1 = '1'
            level2 = self._context["default_higher_two_id"]
            level3 = vals.get('cls_type')
            vals['name'] = level1 + level2 + level3 + self.env['ir.sequence'].next_by_code('mymodule.rules') or '/'
            print(vals['name'])
        res = super(mymodule, self).create(vals)
        res.write_data()
        return res

    @api.model
    def write_data(self):
        warehouse = self.env["ware.house"]
        level4 = models.BaseModel.default_get(self, fields_list=['cls_second', 'cls_one'])
        level5 = level4['cls_second']
        level6 = level4['cls_one']
        warehouse.create({
            'name': self.name,
            'cls_one': level6,
            'cls_second': level5,
            'date': self.date,
            'desc': self.desc,
            'attr_v1': self.attr_v1,
            'attr_v2': self.attr_v2,
            'attr_v3': self.attr_v3,
            'attr_v4': self.attr_v4,
            'attr_v5': self.attr_v5,
        })



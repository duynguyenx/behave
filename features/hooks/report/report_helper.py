from __future__ import print_function
from conf.env_setup import EnvSetup
from features.hooks.report import summary_report_constants as report_constants
import logging
import os
import errno


class ReportHelper(object):

    logger = logging.getLogger(__name__)

    @staticmethod
    def write_scenario_summary(context, scenario, report_path):
        try:
            status_list_to_report = str(EnvSetup.REPORT_SCENARIO_STATUS).split(',')
            if not any(status.lower() == scenario.status for status in status_list_to_report):
                return
            status = report_constants.REPORT_CONFIG['SCENARIO'][scenario.status]['description']
            feature = ReportHelper.get_feature_scenario(scenario)
            case_id = ReportHelper.get_case_id_of_scenario(scenario)
            logging_info = '{status} | {feature} | {case_id} | {name}'.format(
                status=status,
                feature=feature,
                case_id=case_id,
                name=scenario.name)
            print(logging_info, file=open(report_path, 'a'))
        except IOError as io_error:
            ReportHelper.logger.error('errno:', io_error.errno)
            ReportHelper.logger.error('err code:', errno.errorcode[io_error.errno])
            ReportHelper.logger.error('err message:', os.strerror(io_error.errno))

    @staticmethod
    def get_feature_scenario(scenario):
        feature_file_path = scenario.feature.filename
        return os.path.basename(feature_file_path)

    @staticmethod
    def get_case_id_of_scenario(scenario):
        case_id = 'not_defined'
        for tag in scenario.tags:
            if tag.startswith("id-"):
                case_id = tag
        return case_id
